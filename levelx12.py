# # EN
# Codename: levelx12
# Mission: In this mission you receive a string and a number, you must return the string repeated n number of times.
#
# Example:
# HMV(Input): JwSIK 17
#
# Hacker(Output): JwSIKJwSIKJwSIKJwSIKJwSIKJwSIKJwSIKJwSIKJwSIKJwSIKJwSIKJwSIKJwSIKJwSIKJwSIKJwSIKJwSIK

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx12')

log.success('[+] Received levelx12')
level = s.recv(1024)
print(level)

level = level.decode('utf-8').split(' ')
result = level[0]*int(level[1])
print(result)

log.success('[+] Responding to levelx12')
s.send(result.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx12
# b'kAbUb 24'
# kAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUbkAbUb
# [+] [+] Responding to levelx12
# [+] [+] Received Flag!
# Flag: HMV{ztr1ngc0nc4444t3nat3}
# [*] Closed connection to temperance.hackmyvm.eu port 9988