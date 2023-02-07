print('One a Day One Liners with Python - 2023.02.07')
print('Create a year of mock weather data ❄️🌿☀️🍂📈')

from math import cos
from random import uniform

celsius = [(1-cos(d / 60)) * 16 + uniform(-1.5, 1.5) for d in range(0, 365)]
