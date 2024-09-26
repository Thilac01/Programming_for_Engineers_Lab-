# CO1010 Lab 07
# Sub -plots
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# plot the graphs
plt.subplot(1, 2, 1)
plt.plot(x, y1 , "-r")
plt.title("sin(x)", fontsize =18)
plt.xlabel("angle (radians)", fontsize =15)
plt.ylabel("sin(x)", fontsize =15)
plt.grid()
plt.subplot(1, 2, 2)
plt.plot(x, y2 , "g")
plt.title("cos(x)", fontsize =18)
plt.xlabel("angle (radians)", fontsize =15)
plt.ylabel("cos(x)", fontsize =15)
plt.grid()
plt.tight_layout()
plt.show()