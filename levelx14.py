# # EN
# Codename: levelx14
# Mission: In this mission you receive a string and a character, you must return the number
# of times the character is repeated in the string.
#
# Example:
# HMV(Input): Kd5vfizCyqgwN2HlEWq2ZOMkaZmar7rmyCl0ssGf078aJ5J3FJKvLzijiqSbsK8ChhLZ1AI3GVhWnYXixY7J4q7KqKSA8t
# VYsQo0LHjjsGSyLHM9lwi8nVhQA7EUBFo1MJ2gPGo2Nywsz7qlq9C7cKC2xyTdVXVhciK6gMVgRdlOktkx5IMXcnHOSbsnagqDBM56CF87MBT2X
# MvUAPRbiEuZsMSIFGpFcNYAPOGD04def3j6a15xCVosZ9wLJI5cAk07aUxULniLYzWjCk64ZDsvisGlG2wqIFpMwnMG24T52yHCQlwYYRNrTsLs
# awZzcUfeutE00WRvcAPyRAYsJRXqaFX9m9teOIA1UqoZfLkRdur3pla6cJxYGl1hi1REClkarFwCFmOAflXN2BZL8mzzK9wixxsvqx7iCL5ky79
# 0pF74MRXt8t09z2zW20qJTLg2UiAvl1ZQ8uB7JhVojRFY4LdW8bS6rQQ4iQGJwyeAzkNaPzwlQIFLdgt9UhdXIstPo7TotSSG60g1ln9G6w1OPU
# K951lrGrKmrCKEUvoGyL3HkToZtkywcL0eYyrW1BrkPTs95TvoUhLjp5Es3mqE x
#
# Hacker(Output): 9

from pwn import *

HOST = 'temperance.hackmyvm.eu'
PORT = 9988

s = remote(HOST, PORT)

log.success('[+] Introduction to Hackmyvm')
intro = s.recv(1024)
print(intro)

s.send(b'levelx14')

log.success('[+] Received levelx14')
level = s.recv(1024)
print(level)

level = level.decode().split(' ')
result = level[0].count(level[1])

log.success('[+] Responding to levelx14')
s.send(str(result).encode())

log.success('[+] Received Flag!')
flag = s.recv(1024)
print(flag.decode())

# [x] Opening connection to temperance.hackmyvm.eu on port 9988
# [x] Opening connection to temperance.hackmyvm.eu on port 9988: Trying 5.45.101.64
# [+] Opening connection to temperance.hackmyvm.eu on port 9988: Done
# [+] [+] Introduction to Hackmyvm
# b'\n[== HMVLabs Chapter 3: Temperance ==]\nRespect & Have fun!\n|https://hackmyvm.eu|\n\nLevel:\n'
# [+] [+] Received levelx14
# b'iMtJCXlpoLJKpEomMkwAslEtgPBhnQpiNsKAXvlxTOuGPOFjZiGrtuQwvqGCopGUvfvjFomhurAueKdFRlBobSnUpYHtJOgeNmcQzcMSsCnlmaNXuEshGtAkWrKAOEnbgfmhmleZAMhWpoQwLZAETxpzHeOVItWRjaJCmBKHcoxUQYUcZRxaSkKHzFqZfdhkDylRwzTMIkMnGrhrZGcIaaadxYPZNwRPTDGQKTqORbkHfYjYiXiRBFoBhoCHoeYcfFaQUtJioZOfNrgZtOmZYEmSDIMGjxChajvWIJYEiDzJWhaGMcxOuEHBobCbpEEZkkdiDSZvRlcPYKxsjyXCnsVMAzgxHMKDrITaYENjNzbmkEljWiylfPWCQzvsmTJmWlIuMyOSOPUrepKwWWpuxTatVsccYgHqLypKuBjvxofyKlqYDSYXYPoYrpBjgHIQFXcHrHpDctRuKOZmmKJNCAzcAMPYAfglryMOgHBrYAOMiVOMxBOVJeGhCMLqApsNFTXhaBQJRmfvIdfhywGyHpuYXBClADXMYYBRGSKXtZxIOgqPaVmCPVxIfhUHwQNQfloARVFDuUlIwFjZTRsWuZgu J'
# [+] [+] Responding to levelx14
# [+] [+] Received Flag!
# Flag: HMV{f1ndthec0rrectch4r}
# [*] Closed connection to temperance.hackmyvm.eu port 9988
