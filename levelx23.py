# # EN
# Codename: levelx23
# Mission: In this mission you will receive a 5x1 pixel png encoded in base64, you must read the last RGBA
# value of each pixel, convert it to ascii and return the result.
#
# Example:
# HMV(Input): iVBORw0KGgoAAAANSUhEUgAAAAUAAAABCAYAAAAW/mTzAAAAIklEQVR4nGJpk+BMd+Jkvbf
# n02/lr5f+c1U+5TwOCAAA//9bkgoL6P+/xQAAAABJRU5ErkJggg==
#
# Hacker(Output): gEhr9

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

s.send(b'levelx23')

log.success('[+] Received levelx23')
level = s.recv(1024)
print(level)

result = ''
image = Image.open(io.BytesIO(base64.b64decode(level)))
for i in range (image.size[0]):
    for j in range (image.size[1]):
        pixel = image.getpixel((i,j))
        result += chr(pixel[-1])


log.success('[+] Responding to levelx23')
s.send(result.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx23
# b'iVBORw0KGgoAAAANSUhEUgAAAAUAAAABCAYAAAAW/mTzAAAAIklEQVR4nGIusV/pcsv6gf/M7k2Kz0Q/283o2qAECAAA//9pPAn/kzqlwwAAAABJRU5ErkJggg=='
# [+] [+] Responding to levelx23
# [+] [+] Received Flag!
# Flag: HMV{n00bzt3g0}
# [*] Closed connection to temperance.hackmyvm.eu port 9988