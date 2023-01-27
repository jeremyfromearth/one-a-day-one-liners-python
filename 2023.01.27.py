print('One a Day One Liners with Python - 2023.01.26')
print('Auto-detect the delimiter of a CSV file and parse it 🐶')

from csv import reader, Sniffer

with open('./data/csv/web-of-science-20k.csv') as f:
  data = reader(f, Sniffer().sniff(f.read(1024)))

  for i, row in enumerate(data):
    print(row)
    if i > 10: break
