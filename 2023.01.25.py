print('One a Day One Liners - 2023.01.25')
print('Convert a CSV file into a JSON file 🚣🏻‍♀️ → 📦')

import json
from csv import DictReader

with open('./data/csv/web-of-science-20k.csv') as csv_file:
  with open('./data/json/web-of-science-20k.json', 'w') as json_file:
    json_file.write(json.dumps(list(DictReader(csv_file))))
