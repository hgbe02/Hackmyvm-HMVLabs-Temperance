# # EN
# Codename: levelx24
# Mission: In this mission you will receive a URL which you must visit, you must return the string found on the web.
#
# Example:
# HMV(Input): http://temperance.hackmyvm.eu:8090/uwu/3312
#
# Hacker(Output): 4441514

from pwn import *
import requests

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx24')

log.success('[+] Received levelx24')
level = s.recv(1024)
print(level)

url_data = requests.get(level.decode()).text

log.success('[+] Responding to levelx24')
s.send(url_data.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx24
# b'http://temperance.hackmyvm.eu:8090/uwu/8878'
# [+] [+] Responding to levelx24
# [+] [+] Received Flag!
# Flag: HMV{1nt3rn3tw0w}
# [*] Closed connection to temperance.hackmyvm.eu port 9988
