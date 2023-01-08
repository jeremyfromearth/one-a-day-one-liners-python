print('One a Day One Liners - 2023.01.08')
print('Create a Bag of Words model with the Counter module 🔢')

import re
from collections import Counter

with open('./data/text/stop.txt') as f:
  stop = f.read().split('\n')

with open('./data/text/darwin-origin_of_species-pg2009.txt') as f:
  text = f.read().replace('\n', ' ')[:-1]
  terms = filter(lambda s: s.lower() not in stop, re.sub(r'[^\w\s]', '', text).split(' '))
  bow = Counter(terms)

  for i, w in enumerate(bow.most_common(20)):
    print(f'#{i}, term: {w[0]}, count: {w[1]}')
