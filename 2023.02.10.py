print('One a Day One Liners with Python - 2023.02.10')
print('Let’s make some noise 🎧')

from math import cos, sin
from random import randint

w = 512
h = 512
noise = [[cos(x*8/w) * sin(y*8/h) * randint(0, 255) for x in range(w)] for y in range(h)]
