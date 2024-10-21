"""
Lab2: Write a python program using Interpolation to fill in missing values in the data frame. After that store the data frame into a MATLAB file using SciPy IO.Then display the contents from the MATLAB file. 

Input: df = pd.DataFrame({"Math":[12, 4, 7, None, 2], "English":[4, 3, 57, 3, None], "Hindi":[20, 16, None, 3, 8], "Science":[14, 3, None, None, 6]})
"""

import pandas as pd
from scipy.io import savemat, loadmat

# Create the DataFrame
df = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Fill missing values using interpolation
df_interpolated = df.interpolate()

# Display the DataFrame after interpolation
print("\nDataFrame after Interpolation:")
print(df_interpolated)

# Store the DataFrame into a MATLAB file using SciPy I/O
# Convert the DataFrame to a dictionary, as savemat requires a dictionary structure
matlab_data = {'data': df_interpolated.to_dict(orient='list')}
savemat('data.mat', matlab_data)

# Load the MATLAB file and display the contents
loaded_data = loadmat('data.mat')

# Display the contents from the MATLAB file
print("\nContents of the MATLAB file:")
print(loaded_data)

"""
ANSWER=

Original DataFrame:
   Math  English  Hindi  Science
0  12.0      4.0   20.0     14.0
1   4.0      3.0   16.0      3.0
2   7.0     57.0    NaN      NaN
3   NaN      3.0    3.0      NaN
4   2.0      NaN    8.0      6.0

DataFrame after Interpolation:
   Math  English  Hindi  Science
0  12.0      4.0   20.0     14.0
1   4.0      3.0   16.0      3.0
2   7.0     57.0    9.5      4.0
3   4.5      3.0    3.0      5.0
4   2.0      3.0    8.0      6.0

Contents of the MATLAB file:
{'__header__': b'MATLAB 5.0 MAT-file Platform: nt, Created on: Mon Oct 21 11:49:39 2024', '__version__': '1.0', '__globals__': [], 'data': array([[(array([[12. ,  4. ,  7. ,  4.5,  2. ]]), array([[ 4.,  3., 57.,  3.,  3.]]), array([[20. , 16. ,  9.5,  3. ,  8. ]]), array([[14.,  3.,  4.,  5.,  6.]]))]],
      dtype=[('Math', 'O'), ('English', 'O'), ('Hindi', 'O'), ('Science', 'O')])}
      
"""
