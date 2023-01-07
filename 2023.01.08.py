print('One a Day One Liners - 2023.01.08')
print('Generate n-grams ✂️')

with open('./data/text/darwin-origin_of_species-pg2009.txt') as f:
  n = 4
  text = f.read().replace('\n', ' ')[:-1]
  items = text.split(' ')

  n_grams = [(i, i+n, ' '.join(items[i:i+n])) for i in range(0, len(items))]

  print(n_grams[100:110])


