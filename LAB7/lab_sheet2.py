Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
vector = np.array([0.1,0.2,0.3,0.4,0.5,06])
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
import numpy as np
vector = np.array([0.1,0.2,0.3,0.4,0.5,0.6])
np.sin(vector)
array([0.09983342, 0.19866933, 0.29552021, 0.38941834, 0.47942554,
       0.56464247])
mat1 = np.array([1,2],[-1,-2])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    mat1 = np.array([1,2],[-1,-2])
TypeError: Field elements must be 2- or 3-tuples, got '-1'
>>> mat1 = np.array ([[1, 2], [-1, -2]])
>>> mat2 = np.array([[4,5],[-8,-9]])
>>> np.dot(mat1,mat2)
array([[-12, -13],
       [ 12,  13]])
>>> np.linalg.det(mat2)
3.999999999999999
>>> np.linalg.inv(mat2)
array([[-2.25, -1.25],
       [ 2.  ,  1.  ]])
>>> A = np.array([[1,1,1],[0,2,5],[2,5,-1]])
>>> B = np.array([[6,4,27]])
>>> np.linalg.solve(A,B)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    np.linalg.solve(A,B)
  File "C:\Users\thila\AppData\Roaming\Python\Python312\site-packages\numpy\linalg\linalg.py", line 409, in solve
    r = gufunc(a, b, signature=signature, extobj=extobj)
ValueError: solve: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (m,m),(m,n)->(m,n) (size 1 is different from 3)
>>> A = np.array ([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
>>> B = np.array([6, 4, 27])
>>> np.linalg.solve(A, B)
... 
array([ 2.71428571,  4.14285714, -0.85714286])
