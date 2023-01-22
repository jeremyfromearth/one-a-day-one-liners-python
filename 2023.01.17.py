print('One a Day One Liners - 2023.01.17')
print('Multiply two matrices 🅰️ ✖ 🅱️')

a = [
  [1, 2, 3],
  [4, 5, 6]
]

b = [
  [7, 8, 0],
  [9, 10, 0],
  [11, 12, 0]
]

result = [[sum([x * y for x, y in zip(row, col)]) for col in zip(*b)] for row in a]

for i, _ in enumerate(result):
  print(f'{i}: {_}')

# Take a look at what happens when we unpack and unzip b
for i, _ in enumerate(zip(*b)):
  print(f'{i}: {_}')
