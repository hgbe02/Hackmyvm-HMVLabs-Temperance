# # EN
# Codename: levelx20
# Mission: In this mission you receive some of the first 50 words from the Rockyou dictionary in MD5.
# You must send which word the md5 corresponds to.
#
# Example:
# HMV(Input): f25a2fc72690b780b2a14e140ef6a9e0
#
# Hacker(Output): iloveyou

from pwn import *
import hashlib

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx20')

log.success('[+] Received levelx20')
level = s.recv(1024)
print(level)

level = level.decode()
rockyou_md5 = {}
result = ''
with open('./rockyou_top100', 'r', encoding='utf-8') as f:
    rockyou = f.read().strip().split('\n')[0:50]   # 将文件设置为LF，即行分割符为 \n
for word in rockyou:
    if hashlib.md5(word.encode()).hexdigest() == level:
        result = word
        break

log.success('[+] Responding to levelx20')
s.send(result.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx20
# b'1660fe5c81c4ce64a2611494c439e1ba'
# [+] [+] Responding to levelx20
# [+] [+] Received Flag!
# Flag: HMV{r0ckur0ckme}
# [*] Closed connection to temperance.hackmyvm.eu port 9988