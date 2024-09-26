Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np

python_list = [1,2,True,1]
numpy_array = np.array(python_list)
numpy_array
array([1, 2, 1, 1])
>>> type(numpy_array)
<class 'numpy.ndarray'>
>>> 
>>> numpy_array = np.array(python_list)
>>> python_list = ['1','2','Hello','1']
>>> nmpy_array = np.array(python_list)
>>> print(nmpy_array)
['1' '2' 'Hello' '1']
>>> type(nmpy_array)
<class 'numpy.ndarray'>
>>> nmpy_array
array(['1', '2', 'Hello', '1'], dtype='<U5')
>>> numpy_array
array([1, 2, 1, 1])
>>> numpy_array = [1,2,'Hello',1]
>>> numpy_array = np.array(nump_array)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    numpy_array = np.array(nump_array)
NameError: name 'nump_array' is not defined. Did you mean: 'numpy_array'?
>>> numpy_array = np.array(numpy_array)
>>> numpy_array
array(['1', '2', 'Hello', '1'], dtype='<U11')
>>> numpy_array = [1,2,"Hello",1]
>>> numpy_array = np.array(numpy_array)
>>> numpy_array
array(['1', '2', 'Hello', '1'], dtype='<U11')
