print('One a Day One Liners - 2023.01.05')
print('k-permutations of n 🧮')

from functools import reduce
n, k = (10, 4)
permutations = reduce(lambda x, i: x * i, range(1, n + 1)) / reduce(lambda x, i: x * i, range(1, 2 if n == k else n - k))
print(f'P({n}, {k}) = {permutations}')
