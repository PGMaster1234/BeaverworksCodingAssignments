import numpy as np
import matplotlib as mpl
import seaborn as sb

x = np.random.rand(10, 12)
ax = sb.heatmap(x)
sb.scatterplot(x)
