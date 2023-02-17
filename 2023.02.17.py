print('One a Day One Liners with Python - 2023.02.17')
print('Filter out rows of data based on a character range of a given column 🥡')

from csv import reader
from itertools import dropwhile, takewhile
from string import ascii_lowercase as chars

with open('./data/csv/songs.csv') as f:
  data = reader(f)
  data = sorted(data, key=lambda row: row[0])

a, b = 'd', 'm'
filtered = list(
  dropwhile(lambda row: chars.index(row[0][0].lower()) < chars.index(a),
    takewhile(lambda row: chars.index(row[0][0].lower()) <= chars.index(b), data)
  )
)

for row in filtered:
  print(f'{row[0]} - {row[1]}')
