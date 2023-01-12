print('One a Day One Liners - 2023.01.10')
print('Remove stop words 🫣')

import re

with open('./data/text/stop.txt') as f:
  stop = f.read()

with open('./data/text/darwin-origin_of_species-pg2009.txt') as f:
  text = ' '.join(f.read().split('\n'))

  #Remove stop words
  text = ' '.join([word for word in re.sub(r'[^\w\s]', '', text).split(' ') if word.lower() not in stop])

  print(text)
