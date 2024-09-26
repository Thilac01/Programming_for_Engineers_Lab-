# CO1010 Lab 07
# NumPy with for loop
# Import the module
import numpy as np
# Create a matrix of size (3,3)
mat1 = np.reshape(np.arange(0, 9, 1), (3, 3))
# Get the shape of the matrix
(r, c) = mat1.shape
# Print all the values
for x in range(r):
    for y in range(c):
        print("Item @ (%d,%d): %d" % (x, y, mat1[x, y]))
