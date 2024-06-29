# # EN
# Codename: levelx11
# Mission: In this mission you will receive a string in Morse code, you must decode it and return it.
#
# Example:
# HMV(Input): .-- ...- .-. --.. -... --.. ... ..- ...-- .... ..--- -.- ...
# .-- --... .-- .... ---.. -..- ..-. .... .. ----. .-. ....
#
# Hacker(Output): WVRZBZSU3H2KSW7WH8XFHI9RH

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx11')

log.success('[+] Received levelx11')
level = s.recv(1024)
print(level)

Morse_Dic = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.'
    }
decrypto = []
level = level.decode().split(' ')

# solution1
# for word in level:
#     decrypto += list(Morse_Dic.keys())[list(Morse_Dic.values()).index(word)]
#
# log.success('[+] Responding to levelx11')
# s.send("".join(decrypto).encode())

# solution2
for word in level:
    for key, value in Morse_Dic.items():
        if word == value:
            decrypto.append(key)
log.success('[+] Responding to levelx11')
s.send("".join(decrypto).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx11
# b'- -- .-.. --.- .--. --- -... .-- .--. .-.. -.- -- -. .--. - .-- .-. --.. - .--- -.-- - -. .. --..'
# [+] [+] Responding to levelx11
# [+] [+] Received Flag!
# Flag: HMV{d0tz4ndashez}
# [*] Closed connection to temperance.hackmyvm.eu port 9988