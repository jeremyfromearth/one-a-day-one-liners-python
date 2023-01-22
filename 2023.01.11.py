print('One a Day One Liners - 2023.01.10')
print('Remove all punctuation 🔤')

import string

with open('./data/text/darwin-origin_of_species-pg2009.txt') as f:
  text = f.read()
  # Remove all puncuations (Sorry Darwin)
  punc_free_text = text.translate(str.maketrans('', '', string.punctuation))
  print(punc_free_text)
