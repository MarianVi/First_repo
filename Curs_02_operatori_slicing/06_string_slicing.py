# STRING SLICING

import string

alphabet = string.ascii_lowercase       # 'abcdefghijklmnopqrstuvwxyz'

print(alphabet)

'''
String slicing se refera la faptul ca eu pot desprinde bucati dintr-un 
string(lista) si sa le operam separat
'''

# Operatiunea slice end

substring = alphabet[:3]        # :3 - index
print(substring)

# Slice functioneaza asa : [start:end:step]
substring2 = alphabet[1:3]
print(substring2)

# Slice cu stepping   -   adica din cat in cat

substring_step = alphabet[0:20:2]
print(substring_step)       #indecsii impari

substring_step2 = alphabet[1:21:2]
print(substring_step2)      #indecsii pari

