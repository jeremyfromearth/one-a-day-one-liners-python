print('One a Day One Liners with Python - 2023.02.14')
print('Calculate the moving average for stock data 📈')

from csv import reader
from itertools import accumulate
import matplotlib.pyplot as plt

with open('./data/csv/aapl.csv') as f:
  reader = reader(f)
  next(reader)
  data = [float(row[4]) for row in reader]
  data.reverse()

days = 100
smoothing = 2

ema = list(
  accumulate(
    data,
    lambda a, b: (b * (smoothing / (1 + days)) + (a * (1 - (smoothing / (1 + days)))))
  )
)

plt.title('AAPL 2022.02.14 - 2023.02.14')
plt.plot(data)
plt.plot(ema)
plt.show()
