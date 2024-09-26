# CO1010 Lab 07
# Linear Plots
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
# Create data arrays
x = np.linspace(0, 3*np.pi, 1000)

y = np.sin(x)
# plot the graph
plt.plot(x,y,"g")
plt.title("sin(x) x in range [0,3pi]")
plt.xlabel("angle (radians)")
plt.ylabel("sin(x)")
plt.grid()
plt.show()
