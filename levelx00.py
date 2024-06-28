# # EN
# Codename: levelx00
# Mission: On this mission you will receive an string and you should send the same string.
# The code to solve this level in Python can be found here.
#
# Example:
# HMV(Input): HMVLOVESYOU
#
# Hacker(Output): HMVLOVESYOU

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx00')

log.success('[+] Received levelx00')
level = s.recv(1024)
print(level)

log.success('[+] Responding to levelx00')
s.send(level)

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx00
# b'HMVLOVESYOU'
# [+] [+] Responding to levelx00
# [+] [+] Received Flag!
# Flag: HMV{hell0friendz}
# [*] Closed connection to temperance.hackmyvm.eu port 9988