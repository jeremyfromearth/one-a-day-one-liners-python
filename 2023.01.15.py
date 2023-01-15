print('One a Day One Liners - 2023.01.14')
print('Create an identity matrix 🪪')

n = 5
matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

for row in matrix:
  print(row)
