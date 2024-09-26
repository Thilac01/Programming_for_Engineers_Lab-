Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
python_list = [1,2,3,4]
python_list +1
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    python_list +1
TypeError: can only concatenate list (not "int") to list
import numpy as np
numpy_array  = np.array(python_list)
type(numpy_array)
<class 'numpy.ndarray'>
type(python_list)
<class 'list'>
numpy_array + 2
array([3, 4, 5, 6])
1/numpy_array
array([1.        , 0.5       , 0.33333333, 0.25      ])
np.ones((3,2))
array([[1., 1.],
       [1., 1.],
       [1., 1.]])
np.zeros((3,3))
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
np.arange(0,20,1)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])
type(np.arange(1,5,1))
<class 'numpy.ndarray'>
np.reshape(np.arange(0,20,1),(4,5))
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
matrix = np.array([[1,2,3],[-1,-2,-3],[6,7,8]])
matrix
array([[ 1,  2,  3],
       [-1, -2, -3],
       [ 6,  7,  8]])
matrix.shape
(3, 3)
matrix[:2]
array([[ 1,  2,  3],
       [-1, -2, -3]])
matrix[0:1]
array([[1, 2, 3]])
matrix[0]
array([1, 2, 3])
matrix[:,:2]
array([[ 1,  2],
       [-1, -2],
       [ 6,  7]])
matrix[:,:0]
array([], shape=(3, 0), dtype=int32)



>>> 
>>> matrix = np.array([[1,2,3],[-1,-2,-3],[6,7,8]])

>>> matrix[:,0:2]
array([[ 1,  2],
       [-1, -2],
       [ 6,  7]])
>>> matrix[:1,:]
array([[1, 2, 3]])
>>> matrix[:1,:1]
array([[1]])
>>> matrix[:2,:]
array([[ 1,  2,  3],
       [-1, -2, -3]])
>>> matrix[2:,:]
array([[6, 7, 8]])
>>> matrix[1:,:]
array([[-1, -2, -3],
       [ 6,  7,  8]])
