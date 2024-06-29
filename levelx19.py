# # EN
# Codename: levelx19
# Mission: In this mission you will receive a zip file encoded in base64, the zip file contains a .txt file
# which contains a string inside. You should return the string inside the .txt file.
#
# Example:
# HMV(Input): UEsDBBQACAAIAAAAAAAAAAAAAAAAAAAAAAAHAAAASE1WLnR4dKpMCg7NTk5yC6+qCnANyckzt0j1Mwp2KgpK9
# kg1yw4K8TLNdPPPzjExqKzMyQlNLTfLAgQAAP//UEsHCMc6NsY4AAAAMgAAAFBLAQIUABQACAAIAAAAAADHOjbGOAAAADIAAAAHAAA
# AAAAAAAAAAAAAAAAAAABITVYudHh0UEsFBgAAAAABAAEANQAAAG0AAAAAAA==
#
# Hacker(Output): ybSUkcbFWzzPETln78eN2SBrRcHe6kRTJ5iFOkl40yyllUew6j

from pwn import *
import base64
import io
import zipfile

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx19')

log.success('[+] Received levelx19')
level = s.recv(1024)
print(level)

level = base64.b64decode(level.decode())
level_zip = zipfile.ZipFile(io.BytesIO(level))
target_file_name = level_zip.namelist()[0]
for line in level_zip.open(target_file_name).readlines():
    level = line.decode()

log.success('[+] Responding to levelx19')
s.send(level.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx19
# b'UEsDBBQACAAIAAAAAAAAAAAAAAAAAAAAAAAHAAAASE1WLnR4dIryTSwPC0t29AwNzPTKL42KyKrKDw0MjXTzcAstLUlLiUqpSK8I9XaPrKwqTilMSisKAQQAAP//UEsHCPuutiA4AAAAMgAAAFBLAQIUABQACAAIAAAAAAD7rrYgOAAAADIAAAAHAAAAAAAAAAAAAAAAAAAAAABITVYudHh0UEsFBgAAAAABAAEANQAAAG0AAAAAAA=='
# [+] [+] Responding to levelx19
# [+] [+] Received Flag!
# Flag: HMV{z1pandtxtar3h3r3}
# [*] Closed connection to temperance.hackmyvm.eu port 9988