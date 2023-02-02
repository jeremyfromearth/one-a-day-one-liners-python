print('One a Day One Liners with Python - 2023.02.02')
print('Determine if two rectangles overlap ⧉')

from argparse import Namespace as NS

a = NS(l=0, t=0, r=10, b=10)
b = NS(l=4, t=4, r=12, b=12)

intersects = \
  max(min(a.l, a.r), min(b.l, b.r)) < min(max(a.l, a.r), max(b.l, b.r)) and \
  max(min(a.t, a.b), min(b.t, b.b)) < min(max(a.t, a.b), max(b.t, b.b))

assert intersects is True
print('a & b intersect!')

a = NS(l=0, t=0, r=10, b=10)
b = NS(l=12, t=12, r=14, b=14)

intersects = \
  max(min(a.l, a.r), min(b.l, b.r)) < min(max(a.l, a.r), max(b.l, b.r)) and \
  max(min(a.t, a.b), min(b.t, b.b)) < min(max(a.t, a.b), max(b.t, b.b))

assert intersects is False
print('a & b do not intersect!')
