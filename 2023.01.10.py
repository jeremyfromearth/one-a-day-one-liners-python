print('One a Day One Liners - 2023.01.10')
print('Redact a top secret document 🕵')

import re

with open('./data/text/names.txt') as f:
  names = f.read().split('\n')

with open('./data/text/wired-brains-perception.txt') as f:
  text = f.read()
  # Redact names from the article
  redacted = ' '.join([t if t not in names else '*' * len(t) for t in re.sub(r'[^\w\s]', '', text).split(' ')])
  print(redacted)
