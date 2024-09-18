#2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10

import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)
print("3x3 matrix with values ranging from 2 to 10:")
print(matrix)

"""
ANSWER=
3x3 matrix with values ranging from 2 to 10:
[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]

"""
