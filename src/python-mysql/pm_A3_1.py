import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

x = np.linspace(0, 2*np.pi, 100)
y = np.cos(x)

ax.plot(x, y, 'r-')

ax2 = fig.add_axes([0.3, 0.7, 0.4, 0.2])
ax2.plot(x, np.sin(x), 'g-')
ax2.set_title("I can just do anything with axes!")

# plt.savefig("../figures/pm_A3_1.pdf", bbox_inches = 'tight')
plt.show()
