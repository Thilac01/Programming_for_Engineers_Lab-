# CO1010 Lab 07
# Polynomial curve fitting
# Import libraries
import numpy as np
from numpy.polynomial.polynomial import polyval , polyfit
import matplotlib.pyplot as plt
# Generate x, y using the polynomial 10 + x - 2x^2 + x^3
x = np.linspace(1, 10, 30)
y = [polyval(x_ , [10, 1, -2, 1]) for x_ in x]
# Fit the data to 1st and 2nd order polynomials
f1 = polyfit(x, y, deg =1)
f2 = polyfit(x, y, deg =2)
# Evaluate them to estimate y
y_es_1 = [polyval(x_, f1) for x_ in x]
y_es_2 = [polyval(x_, f2) for x_ in x]
# Plot
plt.plot(x, y, "-og"), plt.plot(x, y_es_1 , "b"), plt.plot(x, y_es_2 , "r")
plt.legend (["Data Points", "1st Order", "2nd Order"])
plt.xlabel("X"), plt.ylabel("Y")
plt.grid()
plt.show()
