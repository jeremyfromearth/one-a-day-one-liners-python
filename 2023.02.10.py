print('One a Day One Liners with Python - 2023-02-10')
print('I am 2D noise 🎧')
from random import random

w = 128
h = 128

noise = [[random() for x in range(w)] for y in range(h)]
print(noise)
