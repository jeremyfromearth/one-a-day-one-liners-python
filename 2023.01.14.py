print('One a Day One Liners - 2023.01.14')
print('Count most common phrases of length n 💯')

from datetime import datetime

with open('./data/text/darwin-origin_of_species-pg2009.txt') as f:
  text = f.read()
  terms = ['species of a genus', 'feathers', 'mutation']

  t1 = datetime.now()
  result = [(term, i) for i in range(len(text)) for term in terms if text.startswith(term, i)]
  t2 = datetime.now()
  result = [(term, i) for term in terms for i in range(len(text)) if text.startswith(term, i)]
  t3 = datetime.now()

  print('First completed in', t2 - t1)
  print('Second completed in', t3 - t2)

  for r in result:
    term, start, end = r[0], r[1], r[1] + len(r[0])
    print(term, start, end, text[start:end])
