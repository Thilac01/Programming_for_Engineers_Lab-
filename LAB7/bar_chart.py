# CO1010 Lab 07
# Bar Plots
# Import libraries
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

import numpy as np
# x locations of bars
x = np.arange (7)
money = [100, 200, 100, 150, 70, 40, 80]
plt.bar(x, money , color =["b"] * 7,width=0.8) # i add that width attributes
plt.xticks(x, ("New York", "California", "Texas", "Arizona", "Pennsylvania", "Ohio", "Washington"), fontsize =12)
plt.grid()
plt.ylabel("Cost ($)", fontsize =13)
plt.xlabel("City", fontsize =13)
plt.title("Cost of Living", fontsize =14)
plt.show()