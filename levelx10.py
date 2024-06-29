# # EN
# Codename: levelx10
# Mission: In this mission you will receive numbers separated by spaces, you must return them in order from
# smallest to largest and without separating them with spaces.
#
# Example:
# HMV(Input): 80 37 67 41 31
#
# Hacker(Output): 3137416780

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx10')

log.success('[+] Received levelx10')
level = s.recv(1024)
print(level)

log.success('[+] Responding to levelx10')
level = level.decode().split(" ")
level.sort()
level = "".join([str(i) for i in level])
s.send(level.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx10
# b'57 67 36 30 30'
# [+] [+] Responding to levelx10
# [+] [+] Received Flag!
# Flag: HMV{1mthez0rt3r}
# [*] Closed connection to temperance.hackmyvm.eu port 9988