# Mandelbrot Set
# CO1010 : Lab 07
# Date : 25/09/2024


# 1. Import Libraries
import numpy as np
import matplotlib.pyplot as plt

# 2. Create a Grid of Points
# Define the image size
width, height = 800, 800

# Define the range of values on the complex plane
real = np.linspace(-2, 1, width)  # Real values from -2 to 1
imaginary = np.linspace(-1.5, 1.5, height)  # Imaginary values from -1.5 to 1.5

# Create a 2D grid of complex numbers using np.meshgrid
x, y = np.meshgrid(real, imaginary)
c = x + 1j * y

# 3. Mandelbrot Function
def mandelbrot(c, max_iter):
    # Initialize z. z represents the complex number z_n in the iteration z_n+1 = z_n^2 + c.
    z = np.zeros_like(c)
    
    # Initialize the output array to store the iteration count for each point.
    # The output will be an integer array, where each value represents the number of
    # iterations before the point 'escapes' (i.e., |z| > 2).
    output = np.zeros(c.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(z) <= 2  # Check where |z| <= 2
        z[mask] = z[mask]**2 + c[mask]  # Apply z = z^2 + c to those points
        output[mask] = i  # Update output with the iteration count
    
    return output

# 4. Generate the Mandelbrot Set
max_iterations = 100
mandelbrot_set = mandelbrot(c, max_iterations)

# 5. Plot the Mandelbrot Set
plt.figure(figsize=(10, 10))

# Use plt.imshow() to plot the Mandelbrot set
plt.imshow(mandelbrot_set, extent=[-2, 1, -1.5, 1.5], cmap='inferno')

# Add a title


# 6. Change the Color Scheme (optional)
# You can experiment with different color maps (cmap)
#plt.figure(figsize=(10, 10))
#plt.imshow(mandelbrot_set, extent=[-2, 1, -1.5, 1.5], cmap='plasma')
#plt.title('Mandelbrot Set')
plt.colorbar()
plt.show()
