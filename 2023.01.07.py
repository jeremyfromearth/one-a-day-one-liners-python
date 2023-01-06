print('One a Day One Liners - 2023.01.07')
print('Tokenize text 📚')

import re
from datetime import datetime

with open('./data/text/darwin-origin_of_species-pg2009.txt') as f:
  text = f.read().replace('\n', ' ')[:-1]

  t1 = datetime.now()
  tokens = [(i, t) for i, t in enumerate(re.sub(r'[^\w\s]', '', text).split(' '))]
  t2 = datetime.now()

  print(f'Completed tokenization of {len(tokens)} in {t2 - t1}')
