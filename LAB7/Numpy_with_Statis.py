# CO1010 Lab 07
# NumPy with statistical methods
# Import the module
import numpy as np
# Create a matrix of size (3,3)
mat1 = np.reshape(np.arange(0, 9, 1), (3, 3))
print(mat1)
print("Mean value of all items: %.2f" % np.mean(mat1))
print("Mean value of columns:", np.mean(mat1 , axis =0))
print("Mean value of rows:", np.mean(mat1 , axis =1))
