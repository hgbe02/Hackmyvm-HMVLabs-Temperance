# # EN
# Codename: levelx02
# Mission: In this mission you will receive a string and you must return the same string but converted to uppercase.
#
# Example:
# HMV(Input): wegomakeittrue
#
# Hacker(Output): WEGOMAKEITTRUE

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx02')

log.success('[+] Received levelx02')
level = s.recv(1024)
print(level)

log.success('[+] Responding to levelx02')
s.send(level.upper())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx02
# b'lhjUq'
# [+] [+] Responding to levelx02
# [+] [+] Received Flag!
# Flag: HMV{uPP3rc4z3z}
# [*] Closed connection to temperance.hackmyvm.eu port 9988