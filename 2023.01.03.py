print('One a Day One Liners - 2023.01.03')
print('Find the nclosest matches to a given string, using difflib 🧐')

import difflib

possibilities = [
  'absolute altitude',
  'absorbance',
  'abstract space',
  'accessory cell',
  'adrenergic',
  'adrenalized'
]

word = 'advection fog'

cutoffs = [0.1, 0.2, 0.3, 0.4, 0.5,  0.6, 0.7,  0.8,  0.9]

print(f'Looking for {word} in {", ".join(possibilities)}')

for i, cutoff in enumerate(cutoffs):
  closest = difflib.get_close_matches(word, possibilities, n=2, cutoff=cutoff)
  print(f'Cutoff[{cutoff}]: closest - {", ".join(closest)}')
