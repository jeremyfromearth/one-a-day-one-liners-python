print('One a Day One Liners with Python - 2023.02.05')
print('Create a Poisson distribution 🔔')

from math import exp
from functools import reduce

m = 15
k = m * 2

poisson = [((m**x) * exp(-m)) / reduce(lambda x, y: x*y, range(1, x+1)) for x in range(1, k)]
print(poisson)
