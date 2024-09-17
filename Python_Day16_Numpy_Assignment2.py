"""
2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.
Input: my_list = [1, 2, 3, 4, 5]
"""

import numpy as np

my_list = [1, 2, 3, 4, 5]
array = np.array(my_list)

# Display the array
print("Array:", array)

# Display the first and last index
print("First index:", array[0])
print("Last index:", array[-1])

# Multiply each element by 2 and display the result
multiplied_array = array * 2
print("Multiplied array:", multiplied_array)

"""
ANSWER=
Array: [1 2 3 4 5]
First index: 1
Last index: 5
Multiplied array: [ 2  4  6  8 10]
"""

