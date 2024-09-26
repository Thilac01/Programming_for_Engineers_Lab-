import matplotlib.pyplot as plt
import numpy as np


# This is for make the number set sutable for x value
x = np.arange(-2 * np.pi, 2 * np.pi, np.pi / 24)

# For Handelling Zero Divition error in that Vextical aximtoes region
with np.errstate(divide='ignore', invalid='ignore'):
    y = np.cos(x) / (1 + np.sin(x))

# Usal Graph ploting attibutes
plt.plot(x, y)
plt.title("Plot of y vers x")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend(['$y = \\frac{\\cos(x)}{1 + \\sin(x)}$'], loc='upper left') # using latex formating to get that proper legend
plt.grid()
plt.show()
