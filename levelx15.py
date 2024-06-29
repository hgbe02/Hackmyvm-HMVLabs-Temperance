# # EN
# Codename: levelx15
# Mission: In this mission you receive a series of numbers, you must return what the next number in the series would be.
#
# Example:
# HMV(Input): 59 140 221 302 383
#
# Hacker(Output): 464

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx15')

log.success('[+] Received levelx15')
level = s.recv(1024)
print(level)

level = level.decode().split(' ')
result = int(level[-1]) + (int(level[1]) - int(level[0]))

log.success('[+] Responding to levelx15')
s.send(str(result).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx15
# b'44 79 114 149 184'
# [+] [+] Responding to levelx15
# [+] [+] Received Flag!
# Flag: HMV{s3qu3nz3123}
# [*] Closed connection to temperance.hackmyvm.eu port 9988