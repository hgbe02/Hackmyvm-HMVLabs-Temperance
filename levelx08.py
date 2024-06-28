# # EN
# Codename: levelx08
# Mission: In this mission you will receive 2 numbers, you must return the result of adding both.
#
# Example:
# HMV(Input): 45 77
#
# Hacker(Output): 122

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx08')

log.success('[+] Received levelx08')
level = s.recv(1024)
print(level)

log.success('[+] Responding to levelx08')
temp = level.split()
s.send(str(int(temp[0])+int(temp[1])).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx08
# b'62 40'
# [+] [+] Responding to levelx08
# [+] [+] Received Flag!
# Flag: HMV{1l34rnzum}
# [*] Closed connection to temperance.hackmyvm.eu port 9988