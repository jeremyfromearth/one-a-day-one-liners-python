print('One a Day One Liners with Python - 2023.02.21')
print('Find the partial sum of an exponential sequence 🤯')

print('Linear')
lin = [i for i in range(10)]
partial = [sum(lin[:i+1]) for i in range(len(lin))]
print(lin)
print(partial)

print('Squared')
squared = [i**2 for i in range(10)]
partial = [sum(squared[:i+1]) for i in range(len(squared))]
print(squared)
print(partial)

print('Cubed')
cubed = [i**3 for i in range(10)]
partial = [sum(cubed[:i+1]) for i in range(len(cubed))]
print(cubed)
print(partial)

print('Quartic')
quart = [i**4 for i in range(10)]
partial = [sum(quart[:i+1]) for i in range(len(quart))]
print(quart)
print(partial)

print('Quintic')
quint = [i**5 for i in range(10)]
partial = [sum(quint[:i+1]) for i in range(len(quint))]
print(quint)
print(partial)
