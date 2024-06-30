# # EN
# Codename: levelx30
# Mission: In this mission we must use XOR and send the resulting string.(key=HMV)
#
# Example:
# HMV(Input): <49#0,)'%;:!0.!,
# ,�"?!/
#
# Hacker(Output): tyMafELksowokYfddVZjsswwxcwdDJMGsMKaENYVaLMJDjrRib

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx30')

log.success('[+] Received levelx30')
level = s.recv(1024)
print(level)

key = 'HMV'
result = ''
level = level.decode()
for i in range(len(level)):
    result += chr(ord(level[i]) ^ ord(key[i % 3]))

log.success('[+] Responding to levelx30')
s.send(str(result).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx30
# b"\x11<9\x0c\x14\x00\x1e\n? \x01\x05\x01,1\x1c\x00\x14*\x19\x178*'0\x08\x1f\r\x154\x11\x05>\x0f9\x14&*7\x01=#\x0c\x04\x00\x00#\x1a!\x05"
# [+] [+] Responding to levelx30
# [+] [+] Received Flag!
# Flag: HMV{x0rmex0ru}
# [*] Closed connection to temperance.hackmyvm.eu port 9988