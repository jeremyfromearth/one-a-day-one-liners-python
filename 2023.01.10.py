print('One a Day One Liners - 2023.01.10')
print('Redact a top secret document 🕵')

import re

with open('./data/text/names.txt') as f:
  stop = f.read().split('\n')

# Remove all names from the article
with open('./data/text/wired-brains-perception.txt') as f:
  text = f.read().replace('\n', ' ')[:-1]
  redacted = ' '.join([t if t not in stop else '*' * len(t) for t in re.sub(r'[^\w\s]', '', text).split(' ')])
  print(redacted)
