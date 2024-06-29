# # EN
# Codename: levelx22
# Mission: In this mission you will receive a list of decimal numbers, you must return them converted into their value to ASCII.
#
# Example:
# HMV(Input): 56 116 110 76 90 70 119 49 103 66
#
# Hacker(Output): 8tnLZFw1gB

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx22')

log.success('[+] Received levelx22')
level = s.recv(1024)
print(level)

result = ''
level = level.decode().split(' ')
for i in level:
    result += chr(int(i))

log.success('[+] Responding to levelx22')
s.send(str(result).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx22
# b'77 78 69 73 86 110 122 85 99 120'
# [+] [+] Responding to levelx22
# [+] [+] Received Flag!
# Flag: HMV{4sc111sg00d}
# [*] Closed connection to temperance.hackmyvm.eu port 9988