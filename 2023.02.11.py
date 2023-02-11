print('One a Day One Liners with Python - 2023.02.11')
print('A random walk in a 2D plane with a One Liner 🤔 🚶')

from itertools import accumulate
from random import randint as rand
import matplotlib.pyplot as plt

steps = 100000
walk = list(accumulate([[rand(-1, 1), rand(-1, 1)] for x in range(steps)], lambda p, c: (p[0] + c[0], p[1] + c[1])))

points = list(zip(*walk))
plt.plot(points[0], points[1])
plt.show()
