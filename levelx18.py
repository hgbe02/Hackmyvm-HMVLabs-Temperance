# # EN
# Codename: levelx18
# Mission: In this mission you receive a string and you must return the string converted to binary.
#
# Example:
# HMV(Input): gEmcaIqBNT1z7ikGg1y0RlWZ4ApGvzmOrMBNtHQuycspIMoWDk
#
# Hacker(Output): 0110011101000101011011010110001101100001010010010111000101000010010011100101010000
# 110001011110100011011101101001011010110100011101100111001100010111100100110000010100100110110001010
# 111010110100011010001000001011100000100011101110110011110100110110101001111011100100100110101000010
# 010011100111010001001000010100010111010101111001011000110111001101110000010010010100110101101111010
# 101110100010001101011

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx18')

log.success('[+] Received levelx18')
level = s.recv(1024)
print(level)

result = bin(int(binascii.hexlify(level),16)).replace('0b', '0')

log.success('[+] Responding to levelx18')
s.send(result.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx18
# b'mpWkzVHdVqCkYbPNNSKLOHUAvciddZQBskHrdfFgxzEhVIXnQL'
# [+] [+] Responding to levelx18
# [+] [+] Received Flag!
# Flag: HMV{0n3sandz3r0esuhm}
# [*] Closed connection to temperance.hackmyvm.eu port 9988