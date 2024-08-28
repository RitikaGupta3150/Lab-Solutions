#Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random

# Generate 5 random numbers and store them in a list
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Display the generated random numbers
print("Random numbers:", random_numbers)

# Find the maximum and minimum of the random numbers
maximum = max(random_numbers)
minimum = min(random_numbers)

# Display the maximum and minimum numbers
print("Maximum number:", maximum)
print("Minimum number:", minimum)

"""
ANSWER=
Random numbers: [20, 61, 8, 7, 10]
Maximum number: 61
Minimum number: 7
"""
