print('One a Day One Liners - 2023.01.19')
print('Compute the direct sum of two matrices ⊕')

a = [
  [1, 1, 1, 1],
  [2, 2, 2, 2]
]

b = [
  [3, 3, 3, 3, 3, 3],
  [4, 4, 4, 4, 4, 4]
]

ds = [row + [0] * len(b[0]) for row in a] + [[0] * len(a[0]) + row for row in b]

print(ds)
