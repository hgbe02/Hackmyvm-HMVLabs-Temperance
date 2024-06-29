# # EN
# Codename: levelx21
# Mission: In this mission you will receive a number and you must return what amount of KB that number corresponds to.
#
# Example:
# HMV(Input): 52321
#
# Hacker(Output): 51.09KB

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx21')

log.success('[+] Received levelx21')
level = s.recv(1024)
print(level)

result = int(level.decode()) / 1024
result = format(result, ".2f") + "KB"

log.success('[+] Responding to levelx21')
s.send(result.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx21
# b'91975'
# [+] [+] Responding to levelx21
# [+] [+] Received Flag!
# Flag: HMV{k1l0b33tz}
# [*] Closed connection to temperance.hackmyvm.eu port 9988
