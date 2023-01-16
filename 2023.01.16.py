print('One a Day One Liners - 2023.01.14')
print('Find the transpose a square matrix 🙃')

matrix = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8]
]

transpose = [[matrix[n][m] for n in range(len(i))] for m, i in enumerate(matrix)]

for row in transpose:
  print(row)
