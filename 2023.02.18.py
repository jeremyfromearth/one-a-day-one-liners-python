print('One a Day One Liners with Python - 2023.02.18')
print('Easily generate all r permutations of a given list of items 🪄')

from csv import reader
from itertools import chain, permutations
from random import sample

with open('./data/csv/songs.csv') as f:
  r = 2
  perms = permutations(
    chain.from_iterable([row[0].split(' ') for row in reader(f)]), r
  )

  # This can become very lengthy for large values of r
  # for i in perms:
    # print(' '.join(i).title())

  # Proceed With Caution!

  # This can also take a very long time and consume a lot of memory
  # for large values of r as the iterator is converted into a list
  # Take a random sample
  for p in sample(list(perms), 20):
    print(' '.join(p).title())
