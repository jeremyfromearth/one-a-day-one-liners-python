print('One a Day One Liners with Python - 2023.02.09')
print('Calculate the probability of rolling 8, twice in 10 rolls of a 20 sided die 🎲')

from random import choices

rolls = 10
match = 8
matches = 2
sides = 20
sims = 10000

prob = sum([choices([i for i in range(sides)], k=rolls).count(match) >= matches for i in range(sims)]) / sims
print(prob)
