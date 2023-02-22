print('One a Day One Liners with Python - 2023.02.21')
print('Compute a range of digits from the Fibonacci Sequence 2️⃣ 3️⃣ 5️⃣')

from math import sqrt

n1 = 0
n2 = 20
sq5 = sqrt(5)
phi = (1 + sq5) / 2
fib = [int(round(pow(phi, i) / sq5)) for i in range(n1, n2)]

print('sqrt of 5 = ', sq5)
print('phi = ', phi)

for n in fib:
  print(n)
