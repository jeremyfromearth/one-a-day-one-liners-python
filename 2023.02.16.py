print('One a Day One Liners with Python - 2023.02.16')
print('Group items in tabular data by column 💿')
from csv import reader
from itertools import groupby

with open('./data/csv/songs.csv') as f:
  data = reader(f)
  groups = groupby(sorted(data, key=lambda row: row[3]), lambda row: row[3])

for group in groups:
  print('-' * len(group[0]))
  print(group[0])
  print('-' * len(group[0]))
  for item in group[1]:
    print(f'{item[2]} by {item[0]} from the album {item[1]}')
