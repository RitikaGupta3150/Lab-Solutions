"""
1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 
Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
"""

import numpy as np

# Input temperatures array
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-4,-12])

# Find hot days (temperature > 35°C)
hot_days = temperatures[temperatures > 35]

# Find cold days (temperature < 5°C)
cold_days = temperatures[temperatures < 5]

# Display results
print("Hot days:", hot_days)
print("Cold days:", cold_days)

"""
ANSWER=
Hot days: [36.8 38.7 37.2]
Cold days: [ -4. -12.]

"""
