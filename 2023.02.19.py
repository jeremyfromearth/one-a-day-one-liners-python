print('One a Day One Liners with Python - 2023.02.19')
print('Compute an arithmetic series')

start, end, diff = 5, 100, 5

# A viable, yet naive approach
series = sum([i for i in range(start, end+1, diff)])
print(series)

# Purely analytical solution
series = ((((end-start)/diff)+1) * (start+end)) * 0.5
print(series)
