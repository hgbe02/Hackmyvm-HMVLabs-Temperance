# # EN
# Codename: levelx03
# Mission: In this mission you will receive a string in base64, you must do the decode and return the result.
#
# Example:
# HMV(Input): eW91bWFrZW1lY3J5Cg==
#
# Hacker(Output): youmakemecry

from pwn import *
import base64

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx03')

log.success('[+] Received levelx03')
level = s.recv(1024)
print(level)

log.success('[+] Responding to levelx03')
s.send(base64.b64decode(level))

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx03
# b'cWRoU2NsY3BWSlVDTXpTZnRkdlJPRGdiVg=='
# [+] [+] Responding to levelx03
# [+] [+] Received Flag!
# Flag: HMV{baz364WTF}
# [*] Closed connection to temperance.hackmyvm.eu port 9988