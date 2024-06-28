# # EN
# Codename: levelx04
# Mission: In this mission you will receive a string and you must return it in reverse.
#
# Example:
# HMV(Input): crazycrazycrazycrazy
#
# Hacker(Output): yzarcyzarcyzarcyzarc

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx04')

log.success('[+] Received levelx04')
level = s.recv(1024)
print(level)

log.success('[+] Responding to levelx04')
s.send(level[::-1])

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx04
# b'ooJuKwbLRaLpacaVEMZqaRrUc'
# [+] [+] Responding to levelx04
# [+] [+] Received Flag!
# Flag: HMV{r3vr3vr3v}
# [*] Closed connection to temperance.hackmyvm.eu port 9988