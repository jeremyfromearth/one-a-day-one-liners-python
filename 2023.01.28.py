print('One a Day One Liners - 2023.01.25')
print('Remove all files of a specific type from the current dir 🗑️')

import os
from pathlib import Path

print('Pre delete')
for p in Path('.').glob('*.swp'):
  print(p.resolve())

print('Deleting...')
for p in Path('.').glob('*.swp'): os.remove(p.resolve())

print('Post delete')
for p in Path('.').glob('*.swp'):
  print(p.resolve())
