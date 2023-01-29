print('One a Day One Liners with Python - 2023.01.29')
print('Determine if a point is within a plane 👉🏻 ✈️"')
from argparse import Namespace
p1 = Namespace(x=10, y=10)
plane = Namespace(x1=0, x2=20, y1=0, y2=20)

point_in_plane = p1.x >= plane.x1 and p1.x <= plane.x2 and p1.y >= plane.y1 and p1.y <= plane.y2
print(f'Point: {p1.x}, {p1.y} in Plane: {plane.x1}, {plane.x2}, {plane.y1}, {plane.y2}: {point_in_plane}')


def point_in_plane(p1, plane):
  return p1.x >= plane.x1 and p1.x <= plane.x2 and p1.y >= plane.y1 and p1.y <= plane.y2


p2 = Namespace(x=21, y=5)
p3 = Namespace(x=4, y=21)
p4 = Namespace(x=19, y=20)

print('Running tests')
assert not point_in_plane(p2, plane)
assert not point_in_plane(p3, plane)
assert point_in_plane(p4, plane)

p5 = Namespace(x=11, y=19)
p6 = Namespace(x=3, y=19)
plane = Namespace(x1=10, x2=20, y1=10, y2=20)
assert point_in_plane(p5, plane)
assert not point_in_plane(p6, plane)
print('Passed')
