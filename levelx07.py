# EN
# Codename: levelx07
# Mission: In this mission you will receive a string in hexadecimal format, you must return it converted to ascii.
#
# Example:
# HMV(Input): 68374d4c68434872315843476e384d4e49787258336a376979
#
# Hacker(Output): h7MLhCHr1XCGn8MNIxrX3j7iy

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx07')

log.success('[+] Received levelx07')
level = s.recv(1024)
print(level)

log.success('[+] Responding to levelx07')
s.send(bytes.fromhex(level.decode()))

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx07
# b'5157474642516162746d5250446c657a79746f53476d756163'
# [+] [+] Responding to levelx07
# [+] [+] Received Flag!
# Flag: HMV{zup3rh3x4haha}
# [*] Closed connection to temperance.hackmyvm.eu port 9988