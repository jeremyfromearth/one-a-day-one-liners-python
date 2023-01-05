print('One a Day One Liners - 2023.01.06')
print('Memoize a function 🐘')

import string
from datetime import datetime
from functools import lru_cache

@lru_cache(maxsize=120)
def top_n_terms(filepath, stop=None, n=10):
  """
    - Loads a stop words file
    - Loads a text file
    - Splits the text into individual terms and removes puncuation
    - Counts occurences of tersm
    - Returns the top n occuring terms
  """
  result = {}
  if stop:
    with open(stop) as f:
      stop_words = f.read().split('\n')
  else:
    stop_words = []

  with open(filepath) as f:
    text = ''
    for line in f.readlines():
      text += line.lower().strip() + ' '
    terms = text.split(' ')
    for term in terms:
      if term not in stop_words:
        processed = term.translate(str.maketrans('', '', string.punctuation))
        result[processed] = result.get(processed, 0)
        result[processed] += 1

  top_n = (sorted(result.items(), key=lambda x: x[1])[-n:])
  top_n.reverse()
  return top_n

if __name__ == '__main__':
  n_terms = 32
  stop_path = './data/text/stop.txt'
  text_path = './data/text/darwin-origin_of_species-pg2009.txt'

  print('Running top_n_terms for first time')
  t1 = datetime.now()
  top_n = top_n_terms(text_path, stop_path, n_terms)
  t2 = datetime.now()
  delta_1 = t2 - t1
  print(f'Completed in {delta_1}')

  print('Running top_n_terms for second time')
  t3 = datetime.now()
  top_n = top_n_terms(text_path, stop_path, n_terms)
  t4 = datetime.now()
  delta_2 = t4 - t3
  print(f'Completed in {delta_2}')

  for term, count in top_n:
    print(term, count)
