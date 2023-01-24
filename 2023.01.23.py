print('One a Day One Liners - 2023.01.23')
print('Create timed rotating logs  🪵')

import logging
import time
from logging.handlers import TimedRotatingFileHandler as TRF


logger = logging.getLogger()
logger.addHandler(TRF('./logs/one-liners.log', when='S', interval=5, backupCount=10))

for i in range(32):
  print(f'Logging message {i} - check ./logs dir')
  logger.warning(f'Log message {i}')
  time.sleep(0.5)
