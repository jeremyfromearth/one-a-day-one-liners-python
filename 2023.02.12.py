print('One a Day One Liners with Python - 2023.02.12')
print('Compute the powers of 2 up to N with starmap ✨ 🗺️')

from itertools import starmap
from math import pow

N = 16
p2 = [x for x in starmap(pow, [(2, i) for i in range(0, N)])]

print(p2)
