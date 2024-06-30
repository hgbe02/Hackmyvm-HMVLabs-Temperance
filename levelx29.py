# # EN
# Codename: levelx29
# Mission: In this mission you receive 2 coordinates, you must calculate how many KM there are between them
# and return the result (with 3 decimal).
#
# Example:
# HMV(Input): Lat: 23 Lon: 21 - Lat: 25 Lon: 16
#
# Hacker(Output): 554.830

from pwn import *
from geopy.distance import geodesic
import re

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx29')

log.success('[+] Received levelx29')
level = s.recv(1024)
print(level)

# C:\Users\Administrator>python
# Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> level = "Lat: 23 Lon: 21 - Lat: 25 Lon: 16"
# >>> import re
# >>> addr = re.split(r'[: -]', level)
# >>> number = [word for word in addr if word.isdigit()]
# >>> number
# ['23', '21', '25', '16']
# >>> number[0]
# '23'
# >>> number[1]
# '21'
# >>> number[2]
# '25'
# >>> number[3]
# '16'

addr = re.split(r'[: -]', level.decode())
number = [word for word in addr if word.isdigit()]
float_number = [float(f) for f in number[:4]]
addr_A = (float_number[0],float_number[1])
addr_B = (float_number[2],float_number[3])
result = geodesic(addr_A, addr_B).kilometers
# print(result)
result = str(round(result, 3))
log.success('[+] Responding to levelx29')
s.send(str(result).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx29
# b'Lat: 60 Lon: 19 - Lat: 16 Lon: 17'
# [+] [+] Responding to levelx29
# [+] [+] Received Flag!
# Flag: HMV{wh3r314ml0st}
# [*] Closed connection to temperance.hackmyvm.eu port 9988