print('One a Day One Liners with Python - 2023.02.01')
print('Find the intersection of two rectangles 🚦∩')
from argparse import Namespace

a = Namespace(l=0, t=0, r=3, b=2)
b = Namespace(l=1, t=1, r=5, b=3)

intersection = Namespace(l=max(a.l, b.l), t=max(a.t, b.t), r=min(a.r, b.r), b=min(a.b, b.b))
print(intersection)

r1 = Namespace(l=0, t=0, r=2, b=2)
r2 = Namespace(l=3, t=3, r=5, b=6)

intersection = Namespace(l=max(a.l, b.l), t=max(a.t, b.t), r=min(a.r, b.r), b=min(a.b, b.b))

# This is problematic
# The two rectangles don't actually intersect at all
print(intersection)
