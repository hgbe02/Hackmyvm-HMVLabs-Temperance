# # EN
# Codename: levelx06
# Mission: In this mission you will receive a string and you must return its length. (as string, not as int).
#
# Example:
# HMV(Input): hehehewhf
#
# Hacker(Output): 9

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx06')

log.success('[+] Received levelx06')
level = s.recv(1024)
print(level)

log.success('[+] Responding to levelx06')
s.send(str(len(level)).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx06
# b'mVsIAJfWXBBUYYUfqYBStbhCiEBvIBiCcDkxlGKnPtnJrKzkEMZRySqp'
# [+] [+] Responding to levelx06
# [+] [+] Received Flag!
# Flag: HMV{idkl3ng7hzZz}
# [*] Closed connection to temperance.hackmyvm.eu port 9988