# CO1010 Lab 07
# 3D Plots
# Import libraries
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator , FormatStrFormatter
import numpy as np
# Create a figure object
fig = plt.figure ()
ax = fig.gca(projection="3d")
# Create the data X, Y
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.cos(np.sqrt(X**2 + Y**2))
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap="YlGnBu", linewidth =0, antialiased=False)
# Customize the z axis.
ax.set_zlim (-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator (10))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
# Add a color bar which maps values to colors.
fig.colorbar(surf , shrink =0.5, aspect =5)
plt.show()