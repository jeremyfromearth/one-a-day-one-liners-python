from math import cos, sin, tau

print('Square')
square = [
  (0, 0),
  (10, 0),
  (10, 10),
  (0, 10)
]

centroid = [sum(col) / len(square) for col in zip(*square)]
print(centroid)

print('Rectangle')
rect = [
  (-10, 10),
  (10, 10),
  (10, 0),
  (-10, 0)
]

centroid = [sum(col) / len(rect) for col in zip(*rect)]
print(centroid)

print('Equalateral Triangle')
tri = [
  (0, 0),
  (-10, -10),
  (10, -10)
]

centroid = [sum(col) / float(len(tri)) for col in zip(*tri)]
print(centroid)

print('Right Triangle')
rtri = [
  (0, 10),
  (0, 0),
  (10, 0)
]

centroid = [sum(col) / float(len(rtri)) for col in zip(*rtri)]
print(centroid)

print('Pentagon')
r = 5
n = 5
t = tau / n
pentagon = [(cos(t * i) * r, sin(t * i) * r) for i in range(0, n)]
centroid = [sum(col) / float(len(pentagon)) for col in zip(*pentagon)]
print(centroid)

print('Hexagon')
r = 5
n = 6
t = tau / n
hexagon = [(cos(t * i) * r, sin(t * i) * r) for i in range(0, n)]
centroid = [sum(col) / float(len(hexagon)) for col in zip(*hexagon)]
print(centroid)
