# # EN
# Codename: levelx09
# Mission: In this mission you will receive a string encrypted with ROT13, you must decode it and return the result.
#
# Example:
# HMV(Input): ToaZRw5uyWrk4CaZ1tuKxYWR6
#
# Hacker(Output): GbnMEj5hlJex4PnM1ghXkLJE6# EN
# Codename: levelx09
# Mission: In this mission you will receive a string encrypted with ROT13, you must decode it and return the result.
#
# Example:
# HMV(Input): ToaZRw5uyWrk4CaZ1tuKxYWR6
#
# Hacker(Output): GbnMEj5hlJex4PnM1ghXkLJE6

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx09')

log.success('[+] Received levelx09')
level = s.recv(1024)
print(level)


def rot13(a):
    decrypto = ""
    for i in range(len(a)):
        encrypto = str(a[i])
        if 'a' <= encrypto <= 'm' or 'A' <= encrypto <= 'M':
            encrypto = chr(ord(encrypto) + 13)
        elif 'n' <= encrypto <= 'z' or 'N' <= encrypto <= 'Z':
            encrypto = chr(ord(encrypto) - 13)
        elif encrypto == ' ':
            pass
        decrypto += encrypto
    return decrypto


log.success('[+] Responding to levelx09')
s.send(rot13(level.decode()).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx09
# b'lFGipfyyfJaOWZNkkFlSLbKRv'
# [+] [+] Responding to levelx09
# [+] [+] Received Flag!
# Flag: HMV{r0t13izmyfr1end}
# [*] Closed connection to temperance.hackmyvm.eu port 9988
