#1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np

zeros = np.zeros(10)
ones = np.ones(10)
fives = np.full(10, 5)

print("Array of 10 zeros:", zeros)
print("Array of 10 ones:", ones)
print("Array of 10 fives:", fives)

"""
ANSWER=
Array of 10 zeros: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
Array of 10 ones: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
Array of 10 fives: [5 5 5 5 5 5 5 5 5 5]
"""
