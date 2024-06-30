# # EN
# Codename: levelx26
# Mission: In this mission you will receive a png encoded in base64, you must decode it and send the number found in the image.
#
# Example:
# HMV(Input): iVBORw0KGgoAAAANSUhEUgAAAJYAAAAyCAYAAAC+jCIaAAABL0lEQVR4nOzYQU6zQBiA4fbPfxWX3v8gL
# j1MTRcmhBQ6VN5azPNs1BkzkvAGv/LvBAFhkRAWCWGREBYJYZEQFglhkRAWCWGREBYJYZEQFglhkRAWCWGREBYJYZEQFglhkRA
# Wif97H3h5f7vcWj9/fJ7nvzNd27K3dN6WvZHr5MVNb+LS91v27q1/r63tjZ7Fi1qL5TQYwdYYHglLVPtKZ6zrzXr2v5ZHnki/c
# Z1/3e4zVunWjHX9Ol+fzmlLe7SysPZ+CszPm/689nfuXYOnVeMwrxvcfIbnnNFPhXsN4aOfNPm5p89Y8xloZO/WbLT0rmp+5to
# ecDCHmbE4FmGREBYJYZEQFglhkRAWCWGREBYJYZEQFglhkRAWCWGREBYJYZEQFglhkRAWia8AAAD//6oWtSXo+kn1AAAAAElFTkSuQmCC
#
# Hacker(Output): 7006997
from PIL import Image
from pwn import *
import pytesseract
# python3 -m pip install --upgrade pip
# pip install pytesseract
# pip install tesseract
# sudo apt-get install tesseract-ocr
import base64
import io

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx26')

log.success('[+] Received levelx26')
level = s.recv(1024)
print(level)

level = base64.b64decode(level.decode())
image = Image.open(io.BytesIO(level))
result = pytesseract.image_to_string(image)
log.success('[+] Responding to levelx26')
s.send(str(result).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx26
# b'iVBORw0KGgoAAAANSUhEUgAAAJYAAAAyCAYAAAC+jCIaAAABM0lEQVR4nOzYQUrzQBiA4b8/XsWl9z+ISw9TcRGQME1jm1cy+DwrzVcHIW+TYf7/g4CwSAiLhLBICIuEsEgIi4SwSAiLhLBICIuEsEgIi4SwSAiLhLBICIuEsEgIi4SwSAiLxMvRC17fXq+j65f3j8tovly/N1vPb822/mY0Xz4zus7JLTd3FN2e2a35vc/dW3P5fWttHpO/Co94GmytsZ59/bw3FE+qThrW2W/cmf+32R2+x1p8f8UtN3D0NNkzW685mo3sWZOJPbvHGu2Djti3bV3jOdMcN3jSzOXwsH77279+3Z19X/dXJDfg0bOqI864fnKONfoSiBJObJo9FnMRFglhkRAWCWGREBYJYZEQFglhkRAWCWGREBYJYZEQFglhkRAWCWGREBYJYZH4DAAA///wRrNC5WgnbgAAAABJRU5ErkJggg=='
# [+] [+] Responding to levelx26
# [+] [+] Received Flag!
# Flag: HMV{c4ptchm3numb3rz}
# [*] Closed connection to temperance.hackmyvm.eu port 9988