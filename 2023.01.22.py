print('One a Day One Liners - 2023.01.22')
print('Apply a function over each line of a file 📄')

from collections import Counter
from datetime import datetime

line_counter = 0
kw_counter = Counter()
FILE = './data/csv/web-of-science-20k.csv'


def count_keywords(line: str) -> None:
  """
    Count keywords from a given line
  """
  global line_counter
  line_counter += 1
  cols = line.split(',')

  # Only count key words for class 0
  if cols[0] == '0':
    kws = filter(
      lambda x: len(x),
      map(lambda x: x.strip(), cols[5].split(' ')))

    kw_counter.update(kws)


# Apply the count_keywords function line by line
t1 = datetime.now()
for line in open(FILE): count_keywords(line)
t2 = datetime.now()

print(f'Parsed keywords from {line_counter} lines in {t2-t1}')
for kw in kw_counter.most_common(32):
  print(kw)

# Apply the count_keywords function to each line
# after reading the whole file
kw_counter = Counter()
t3 = datetime.now()
with open(FILE) as f:
  lines = f.read().split('\n')
  for line in lines:
    count_keywords(line)
t4 = datetime.now()

print(f'Parsed keywords after reading whole file in {t4-t3}')
for kw in kw_counter.most_common(32):
  print(kw)
