# # EN
# Codename: levelx05
# Mission: In this mission you will receive a string and you must return the last 5 chars.
#
# Example:
# HMV(Input): IDKWhyimdoingthisshit
#
# Hacker(Output): sshit
#
from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx05')

log.success('[+] Received levelx05')
level = s.recv(1024)
print(level)

log.success('[+] Responding to levelx05')
s.send(level[-5::1])

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx05
# b'CAPhNaxlmNQPzkTvDZvfGKODP'
# [+] [+] Responding to levelx05
# [+] [+] Received Flag!
# Flag: HMV{l4ztf1v3wh0t}
# [*] Closed connection to temperance.hackmyvm.eu port 9988