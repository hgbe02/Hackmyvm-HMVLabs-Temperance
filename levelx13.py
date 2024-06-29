# # EN
# Codename: levelx13
# Mission: In this mission you receive a list of strings, you must sort them alphabetically and return the last string in the list.
# The characters "[" and "]" must be removed.
#
# Example:
# HMV(Input): [QJIFc brxkaCWxRDNRMjMDNQBcYPi wpzZBxlRMrvchppNmZcsSsqnSxQd nWxEVnDjUIWObjfZ gfsqzTsgfYYVjx wDeVgobCvrlaM cLFTLXrpnmSYsVaaTDnVArG
# dRbEsX KenQzY ZhDilcASluwhjcHlOrrX nPVXUIZELLdcm RsSrmYVHvonLJnv]
#
# Hacker(Output): wpzZBxlRMrvchppNmZcsSsqnSxQd

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx13')

log.success('[+] Received levelx13')
level = s.recv(1024)
print(level)

level = level.decode().split(" ")
level.sort()
result = level[-1].replace('[', '').replace(']', '')

log.success('[+] Responding to levelx13')
s.send(result.encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx13
# b'[TAvweqyntrNyqTsrwcyKqRmll oewREVOjFBjJktASQOfWT gtyXcaMbgyTGrGhvnNpTxcAfMYhsaI FerkyHRuwCoPWLvLUyNbEaMpoG BtfNmovOAHfeMRhiNDyxgTvYS xKptUemiWwqDxhIPkzWRpIUiZ gCKayWZxEzLujGxdoczjVE ctkskqthXdWYozIyAreUoIAORsKAKx mbmZutQZpr tuobpE YzEAOMlAodubFCIg JZaJhPFlRcmWwwAeJJMUuco]'
# [+] [+] Responding to levelx13
# [+] [+] Received Flag!
# Flag: HMV{WTF1zthatl3vel}
# [*] Closed connection to temperance.hackmyvm.eu port 9988