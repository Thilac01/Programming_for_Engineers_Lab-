import numpy as np
from numpy.polynomial.polynomial import polyval

coeff = [1,0,3,1]
print(np.roots(coeff))

print(polyval(2,[9,4,1]))
print(polyval(1,[9,4,1]))
