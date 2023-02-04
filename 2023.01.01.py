print('One a Day One Liners - 2023.01.01')
print('Generate a random eight character id! 🥇')

import random, string
uid = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

print(f'Here is your randomly generated 8 char id {uid}')

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(
    prog='One a Day One Liner: 2023.01.01',
    description='Tests a random id generating Python One Liner'
  )

  parser.add_argument(
    '-l',
    '--length',
    default=8,
    type=int,
    help='Length of each id'
  )

  parser.add_argument(
    '-c',
    '--count',
    default=100,
    type=int,
    help='Number of ids to generate'
  )

  parser.add_argument(
    '-e',
    '--epochs',
    default=1,
    type=int,
    help='Number of epochs to run'
  )

  args = parser.parse_args()
  length = args.length
  count = args.count
  epochs = args.epochs

  collisions = 0
  letters = string.ascii_letters + string.digits

  print(f'Generating {count} random ids every {epochs} epoch(s)')

  for e in range(epochs):
    lookup = {}
    for i in range(count):
      uid = ''.join(random.choices(letters, k=length))
      if uid in lookup:
        collisions += 1
      lookup[uid] = True

  print(f'Completed with {collisions} collisions')
