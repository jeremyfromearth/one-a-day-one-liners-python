print('One a Day One Liners - 2023.01.18')
print('Partition a matrix into a sub-matrix 🍕')

a = [
  [0, 1, 2, 3, 4, 5],
  [5, 4, 3, 2, 1, 0],
  [2, 4, 6, 8, 10, 12],
  [3, 6, 9, 12, 15, 18]
 ]

x, y = [0, 2], [1, 4]
sub = [m[y[0]:y[1]] for m in a[x[0]:x[1]]]

print(sub)
