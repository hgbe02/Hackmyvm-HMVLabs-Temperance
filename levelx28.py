# # EN
# Codename: levelx28
# Mission: In this mission you receive a JWT token. You must decode it and send the value of the HMVKey. (Default key).
#
# Example:
# HMV(Input): eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJITVZLZXkiOiJVbHFlc0h0bHZIQVdEYVAifQ.65O1aZHiVaGep-QA0-LZRnWXcDF8bZT_E7BXvXaYMUI
#
# Hacker(Output): UlqesHtlvHAWDaP

from pwn import *
import jwt

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx28')

log.success('[+] Received levelx00')
level = s.recv(1024)
print(level)

result = jwt.decode(level.decode(), "secret", algorithms=['HS256']).get('HMVKey')

log.success('[+] Responding to levelx28')
s.send(result.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx00
# b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJITVZLZXkiOiJ1TUxWZHRybkJ6REd3SGsifQ.1o9YdbNk1xrQu4nt5ZGXTK6CwHFEbKJ3jb7CGBR7Ojo'
# [+] [+] Responding to levelx28
# [+] [+] Received Flag!
# Flag: HMV{jWth4f4ck}
# [*] Closed connection to temperance.hackmyvm.eu port 9988