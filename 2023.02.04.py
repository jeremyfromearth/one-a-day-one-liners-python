print('One a Day One Liners with Python - 2023.02.04')
print('Generate a grid of rectangles 🟥 🟧 🟨')

from argparse import Namespace as NS

r = 4
c = 6
w = 5
h = 10
grid = [[NS(l=j*w, r=j*w+w, t=i*h, b=i*h+h) for j in range(c)] for i in range(r)]

print(grid)
