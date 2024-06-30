# # EN
# Codename: levelx32
# Mission: In this mission you receive an md5 and a string. You must permute the string until it matches md5 and return the string.
#
# Example:
# HMV(Input): c142e7e8b1d42f4d6f36dfa760174b3a KOSltuvxy
#
# Hacker(Output): OSylutxKv

from pwn import *
import hashlib
import itertools

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx32')

log.success('[+] Received levelx32')
level = s.recv(1024)
print(level)

level = level.decode().split(" ")
md5 = level[0]
string = list(level[1])
result = ''
for word in itertools.permutations(string):
    result = ''.join(word)
    if hashlib.md5(result.encode()).hexdigest() == md5:
        break

log.success('[+] Responding to levelx32')
s.send(str(result).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx32
# b'edf24066dc8fb06ceea8d58797931413 CJKZimpps'
# [+] [+] Responding to levelx32
# [+] [+] Received Flag!
# Flag: HMV{p3rmut4t10n0np3r}
# [*] Closed connection to temperance.hackmyvm.eu port 9988