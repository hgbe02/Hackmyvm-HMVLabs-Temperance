# # EN
# Codename: levelx31
# Mission: In this mission you receive a png encoded in base64, you must decode it, read the QR code found inside
# and return the string that indicates the QR.
#
# Example:
# HMV(Input): iVBORw0KGgoAAAANSUhEUgAAAGQAAABkEAAAAAAFGRbLAAABn0lEQVR4nOyazW7EMAiEm2rf/5W3J1+IED8mzXg033GbxhnhERjz+
# X5/KPh9+wOmkBA0JAQNCUHjY3+4rt6LvHy03hf9fXc9mohICBo3jyyyNZi3x6037HP2/bvr0UREQtBwPbLw9mQ3b0ReqK63oImIhKARemSXyDNT0EREQtB
# 4zCPZGmwKmohICBqhR7p72Z5Dst7orkcTEQlBw/VIt9/kYT1jvbC7Hk1EJASNa7rm+a/zh4UmIhKChns/4vVsPdbzUX7o5g/1tU6DRkg6j0zt9YjoPsXLU
# zQRkRA02ueRqie8PZ69D4lqOJqISAga5VmU6kyJ54VqXlKtdRo0Qm4eiWoaS7ZPlX1vNn+p1kKHRsj2vFa1JvLY9Q5NRCQEjfG5324+6XpyQRMRCUFjfO4
# 3u/e7s42qtU6BRsj43K/9v6iflZ2dV1/rNGiEPDbTmO1nRbWY/d2DJiISgsbjc79RPvCeq575aSIiIWiMz/1m+1LReaP6HTQRkRA0xud+s3eJ1fyi88hp0
# AgZn/t9C5qISAgaEoKGhKDxFwAA//9Pk6bevZKZBwAAAABJRU5ErkJggg==
#
# Hacker(Output): xfZfsIM
import io
from pwn import *
from PIL import Image
import pyzbar.pyzbar as pyzbar

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx31')

log.success('[+] Received levelx31')
level = s.recv(1024)
print(level)

result = ''
level = base64.b64decode(level)
image = Image.open(io.BytesIO(level))
encode = pyzbar.decode(image)
for e in encode:
    result += e.data.decode('utf-8')

log.success('[+] Responding to levelx31')
s.send(result.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx31
# b'iVBORw0KGgoAAAANSUhEUgAAAGQAAABkEAAAAAAFGRbLAAABpElEQVR4nOyawY7EMAhDt6v5/1+eOeWSChkoVV3L77ajJKxFKCHh8/3+SfD/9D8whYWwYSFsWAgbn/2H4+gttOejaJ3suKo9GY9YCBunGFlkz2Boj2fXuWpPxiMWwkYYI4tsPtjHo3yB5mftLWQ8YiFswBjpEsXKXXcEMh6xEDZui5GdFRtR7FxFxiMWwgaMke5ejs5aaL2uPRmPWAgbYYx075uidVAeuWpPxiMWwsYxfebJ1ubTyHjEQtgI30f27z5ijY/mXc0fvtd6GzJC2jV79u4W/R2tW63tZTxiIWycYiTao9n8gmr16jrZs5uMRyyEjXQvSvb7Hs2v5pNqDS/jEQthA9bs1b1azSORHeeRtyMjZPx9pPtGuMcEykfuaWRHRsgpj0z14Z4MJfNJNA/ZkfGIhbAx3vebjYXsmSyy5zzCjoyQ8b7ffV72niyah35fyHjEQti4raex+n6C6hG/Ib4NGSGP9/2iWMjWRzIesRA2xu+1uu/vaDxCxiMWwsZ43y+q0bvvI65H3oaMkPG+36eQ8YiFsGEhbFgIG78AAAD//2UBpOf1VawdAAAAAElFTkSuQmCC'
# [+] [+] Responding to levelx31
# [+] [+] Received Flag!
# Flag: HMV{4rtQRc0d3z}
# [*] Closed connection to temperance.hackmyvm.eu port 9988