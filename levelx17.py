# # EN
# Codename: levelx17
# Mission: In this mission you receive a 1 pixel png encoded in base64, you must decode it and return the last RGBA value.
#
# Example:
# HMV(Input): iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAEUlEQVR4nGI6OPmFIiAAAP//Br0CYI/JSpAAAAAASUVORK5CYII=
#
# Hacker(Output): 33

from pwn import *
import base64
import io
from PIL import Image

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx17')

log.success('[+] Received levelx17')
level = s.recv(1024)
print(level)

image = Image.open(io.BytesIO(base64.b64decode(level)))
result = image.getpixel((0,0))[-1]

log.success('[+] Responding to levelx17')
s.send(str(result).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx17
# b'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAEUlEQVR4nGL6w86yDBAAAP//BMIBsPZLoOcAAAAASUVORK5CYII='
# [+] [+] Responding to levelx17
# [+] [+] Received Flag!
# Flag: HMV{RGBAsteg0u}
# [*] Closed connection to temperance.hackmyvm.eu port 9988