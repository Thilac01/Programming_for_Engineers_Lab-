# Graph Plotting
# CO1010 : Lab 07
# Date : 25/09/2024

# To import nessasarry library
import numpy as np
import matplotlib.pyplot as plt

# For Gert X value in between  this range
x = np.linspace(-2, 2, 100)

# Formula we wanna  use
y = x**5 - 5*x**3 + 4*x
x_roots = np.roots([1,0,-5,0,4,0])
y_roots = np.zeros(len(x_roots))
plt.scatter(x_roots,y_roots,c='Red')
print(x_roots)
# Calculate the numerical derivative
y_1 = (x + 1e-10)**5 - 5*(x + 1e-10)**3 + 4*(x + 1e-10)
f_prime = (y_1 - y) / 1e-10

# Calculate the integral using cumulative trapezoidal integration
integral_y = np.zeros_like(y) #creates a new array filled with zeros that has the same shape and type as a given array
for i in range(1, len(x)):
    integral_y[i] = integral_y[i - 1] + (y[i - 1] + y[i]) * (x[i] - x[i - 1]) / 2

# To Plot the graphs
plt.plot(x, y, label='y = x^5 - 5x^3 + 4x')
plt.plot(x, f_prime, label='Derivative of y(x)', linestyle='--')
plt.plot(x, integral_y, label='Integral of y(x)', linestyle=':')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function, Numerical Derivative, and Integral')
plt.legend(loc='lower center')
plt.grid()
plt.show()
