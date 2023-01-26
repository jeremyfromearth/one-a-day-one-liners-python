print('One a Day One Liners with Python - 2023.01.26')
print('Search all files in a directory for a term or phrase 🔍')

import os

kw = 'travel'
fpath = './data/text'
matches = [
  [(f, l.strip()) for l in open(f'{fpath}/{f}') if kw in l] for f in os.listdir(fpath)
]

for f in matches:
  for match in f:
    print(match)
