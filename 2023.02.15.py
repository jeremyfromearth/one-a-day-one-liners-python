print('One a Day One Liners with Python - 2023.02.15')
print('Unleash chaos into Universe by computing values of the Logistic Map 💥')
import matplotlib.pyplot as plt

from itertools import accumulate, repeat
from matplotlib.animation import FuncAnimation

# Number of frames to animate
frames = 1000

# The logistic map function
lm = lambda r: [round(x, 2) for x in accumulate(repeat(0.1, 100), lambda x, _: r*x*(1-x))]

# Data for the plot
data = [lm(2 + r/frames * 2) for r in range(frames)]

# Initialize the plot
fig, ax = plt.subplots(1, 1)
def animate(i):
  ax.clear()
  ax.plot(data[i])
  ax.set_title(f'r = {round(2 + 2 * i/1000, 3)}')
  ax.set_ylim([0, 1])

# Save the animation
ani = FuncAnimation(fig, animate, frames=frames, interval=60, repeat=True)
ani.save('./data/img/logistic-map.gif', dpi=120)
plt.close()
