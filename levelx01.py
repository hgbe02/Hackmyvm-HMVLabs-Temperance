# # EN
# Codename: levelx01
# Mission: This mission is similar to the previous one, but adding a minimum of complexity :)
# You will receive a string, you must return the same string and you will
# receive another string which you must also return.
#
# Example:
# HMV(Input): ImString1!
#
# Hacker(Output): ImString1!
#
# HMV(Input): ImString2!
#
# Hacker(Output): ImString2!

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx01')

log.success('[+] Received levelx00')
level = s.recv(1024)
print(level)

log.success('[+] Responding to levelx01')
s.send(level)

log.success('[+] Received levelx01')
level = s.recv(1024)
print(level)

log.success('[+] Responding to levelx01')
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
# b'HMVTEACHING'
# [+] [+] Responding to levelx01
# [+] [+] Received levelx01
# b'NOOBSKILLZ'
# [+] [+] Responding to levelx01
# [+] [+] Received Flag!
# Flag: HMV{3ch03zlol}
# [*] Closed connection to temperance.hackmyvm.eu port 9988