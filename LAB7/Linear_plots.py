# CO1010 Lab 07
# Multiple Linear Plots
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
# Create data arrays
x = np.linspace(0, 3*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# Plot the graphs
plt.plot(x, y1 , '-or')
plt.plot(x, y2 , '--g')
# Format the figure
plt.title("sin(x) and cos(x) in range [0, 3pi]", fontsize =18)
plt.xlabel("angle (radians)", fontsize =15)
plt.ylabel("sin(x),cos(x)",fontsize =15)
plt.legend (["sin(x)","cos(x)"],fontsize =15)
plt.grid()
plt.show()