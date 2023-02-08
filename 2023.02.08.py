print('One a Day One Liners with Python - 2023.02.08')
print('Never make a choice on your own again, with a Magic 8 Ball One Liner 🎱')

from random import choice

q = input('Ask the Magic Eight Ball for advice...\n')
print(choice(open('./data/text/eightball.txt').readlines()))
