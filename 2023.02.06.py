from random import randint, seed
from string import ascii_letters, digits

n = 64
seed(0)
chars = ascii_letters + digits
key = ''.join([chars[randint(0, len(chars)-1)] for _ in range(n)])

print(key)
