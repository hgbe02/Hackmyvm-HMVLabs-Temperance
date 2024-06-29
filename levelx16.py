# # EN
# Codename: levelx16
# Mission: In this mission you receive a png encoded in base64, you must decode it and return
# the size in pixels of its width and height.
#
# Example:
# HMV(Input): iVBORw0KGgoAAAANSUhEUgAAADQAAABeCAYAAABsFzfXAAAAfUlEQVR4nOzPAQkAMBBFobH+oa/G46MN/G+MUJ1QnVCdU
# J1QnVCdUJ1QnVCdUJ1QnVCdUJ1QnVCdUJ1QnVCdUJ1QnVCdUJ1QnVCdUJ1QnVCdUJ1QnVCdUJ1QnVCdUJ1QnVCdUJ1QnVCdUJ1QnVCdUJ1QnVC
# dUN1c6AIAAP//yOQAvaQI2KYAAAAASUVORK5CYII=
#
# Hacker(Output): 52x94

from pwn import *
import base64
from PIL import Image
import io

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx16')

log.success('[+] Received levelx16')
level = s.recv(1024)
print(level)

image = Image.open(io.BytesIO(base64.b64decode(level)))
result = str(image.size[0]) + "x" + str(image.size[1])

log.success('[+] Responding to levelx16')
s.send(result.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx16
# b'iVBORw0KGgoAAAANSUhEUgAAADUAAAAjCAYAAAA0aUL2AAAAQElEQVR4nOzPAQ0AAAjAIGf/0Oa4gwbsPCRVIVUhVSFVIVUhVSFVIVUhVSFVIVUhVSFVIVUhVSFVIVVxAQAA//81twBH1Y1X/QAAAABJRU5ErkJggg=='
# [+] [+] Responding to levelx16
# [+] [+] Received Flag!
# Flag: HMV{p4int3rPNGfile}
# [*] Closed connection to temperance.hackmyvm.eu port 9988