print('One a Day One Liners with Python - 2023.02.13')
print('Run a batch process using iter and islice 🍪')

from itertools import islice

n = 6
it = iter([i for i in range(100)])
while batch := tuple(islice(it, n)): print(batch)
