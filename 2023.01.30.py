print('One a Day One Liners with Python - 2023.01.30')
print('Generate geometry for an n-sided regular polygon ▲ ⬣')

from math import cos, sin, tau

r = 5
n = 6
t = tau / n
hexagon = [(cos(t * i) * r, sin(t * i) * r) for i in range(0, n)]

for i, p in enumerate(hexagon):
  print(f'{i}: (x: {round(p[0], 2)}, y: {round(p[1], 2)})')
