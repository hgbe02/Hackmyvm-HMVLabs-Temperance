# # EN
# Codename: levelx25
# Mission: In this mission you will receive a URL which you must visit, you must return
# the value found in a header (HMV-Header).
#
# Example:
# HMV(Input): http://temperance.hackmyvm.eu:8090/head/673
#
# Hacker(Output): 917182

# curl -s -i http://temperance.hackmyvm.eu:8090/head/673/
# HTTP/1.1 200 OK
# Hmv-Code: 917182
# Date: Sun, 30 Jun 2024 05:54:07 GMT
# Content-Length: 3
# Content-Type: text/plain; charset=utf-8
#
# 673

from pwn import *
import requests

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx25')

log.success('[+] Received levelx25')
level = s.recv(1024)
print(level)

url_data = requests.get(level.decode()).headers['Hmv-Code']
log.success('[+] Responding to levelx25')
s.send(url_data.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx25
# b'http://temperance.hackmyvm.eu:8090/head/5208'
# [+] [+] Responding to levelx25
# [+] [+] Received Flag!
# Flag: HMV{h3ad3rc0ntr0l}
# [*] Closed connection to temperance.hackmyvm.eu port 9988