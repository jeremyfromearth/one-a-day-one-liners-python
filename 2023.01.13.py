print('One a Day One Liners - 2023.01.13')
print('Count most common phrases of length n 💯')

import re
from collections import Counter

with open('./data/text/darwin-origin_of_species-pg2009.txt') as f:
  text = ' '.join(f.read().split('\n'))
  tokens = re.sub(r'^[\w\s]', '', text).lower().split(' ')

  n = 8
  top_n = 50
  phrases = Counter([' '.join(tokens[i:i + n]) for i in range(0, len(tokens))]).most_common(top_n)

  for i, (phrase, count) in enumerate(phrases):
    if len(phrase.strip()):
      print(f'{i}: {phrase} - ({count} times)')
