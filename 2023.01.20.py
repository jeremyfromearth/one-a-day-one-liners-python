print('One a Day One Liners - 2023.01.19')
print('Calculate the cosine similarity of two vectors ← ↑ →')
from math import acos, sqrt, pi

a = [1, 3, -5]
b = [-1, -3, 5]

dot = sum([x*y for x,y in zip(a,b)])

sim = sum([x*y for x,y in zip(a,b)]) / (sqrt(sum([i**2 for i in a])) * (sqrt(sum([i**2 for i in b]))))

angle = acos(sim)

print('A:', a)
print('B:', b)
print('Dot Product:', dot)
print('Cosine Similarity:', sim)
print('Angle Between:', angle)

print('Testing results')
assert dot == -35
assert sim == -1
assert angle == pi
print('Passed!')
