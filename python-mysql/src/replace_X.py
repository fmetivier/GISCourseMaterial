# -*- coding: utf-8 -*-
"""

Tick replacement
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap


N = np.random.randint(1, 10, 5)
X = range(len(N))
T = ['un', 'deux', 'trois', 'quatre', 'cinq']

plt.figure()
plt.bar(X, N)
plt.xticks(X, T);

plt.show()
