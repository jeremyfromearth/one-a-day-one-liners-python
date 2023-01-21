print('One a Day One Liners - 2023.01.21')
print('Calculate the Frobenius norm of a matrix √')
from math import sqrt

a = [
  [0, 1, 2, 3],
  [4, 5, 6, 7]
]

f_norm = sqrt(sum([sum([j**2 for j in i]) for i in a]))

test = sqrt(0**2 + 1**2 + 2**2 + 3**2 + 4**2 + 5**2 + 6**2 + 7**2)

print(test, f_norm)

assert test == f_norm
