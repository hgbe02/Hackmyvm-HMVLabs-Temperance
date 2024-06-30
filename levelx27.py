# # EN
# Codename: levelx27
# Mission: In this mission you will receive a URL which you must visit, in the body of the
# URL there is data from a /etc/passwd file, you must return the UID of the proxy user.
#
# Example:
# HMV(Input): http://temperance.hackmyvm.eu:8090/cumment/3390/
# HMV(Web Body): ---SNIP--- proxy:x:4735654:13:proxy:/bin:/usr/sbin/nologin ---SNIP---
#
# Hacker(Output): 4735654
# curl -i -s http://temperance.hackmyvm.eu:8090/cumment/3390/
# HTTP/1.1 200 OK
# Date: Sun, 30 Jun 2024 06:29:31 GMT
# Content-Length: 630
# Content-Type: text/plain; charset=utf-8
#
#
# root:x:0:0:root:/root:/bin/bash
# daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
# bin:x:2:2:bin:/bin:/usr/sbin/nologin
# sys:x:3:3:sys:/dev:/usr/sbin/nologin
# sync:x:4:65534:sync:/bin:/bin/sync
# games:x:5:60:games:/usr/games:/usr/sbin/nologin
# man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
# lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
# mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
# news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
# uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
# proxy:x:4552485:13:proxy:/bin:/usr/sbin/nologin
# www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
# backup:x:34:34:backup:/var/backups:/usr/sbin/nologin

from pwn import *
import requests

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx27')

log.success('[+] Received levelx27')
level = s.recv(1024)
print(level)

result = ''
url_data = requests.get(level.decode()).text.split('\n')
for line in url_data:
    if 'proxy' in line:
        result = line.split(':')[2]
log.success('[+] Responding to levelx27')
s.send(str(result).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx27
# b'http://temperance.hackmyvm.eu:8090/cumment/1416'
# [+] [+] Responding to levelx27
# [+] [+] Received Flag!
# Flag: HMV{pr0xykn0wur1d}
# [*] Closed connection to temperance.hackmyvm.eu port 9988