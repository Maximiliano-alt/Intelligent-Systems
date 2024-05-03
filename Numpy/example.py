import matplotlib as plt
import matplotlib.pyplot
import pandas as pd
import numpy as np

x = np.linspace (0,2*np.pi, 100)
f = np. sin(x)
g = np.log(1+x)
fig = plt.pyplot.figure()
ax = plt.pyplot.gca()
ax.plot(x, f)
ax.plot(x, g)

fig.show()