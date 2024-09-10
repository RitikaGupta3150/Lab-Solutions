#3. Write a Python program to find duplicate values from a list and display those

# Python program to find duplicate values from a list using a dictionary

numbers = [1, 2, 3, 4, 5, 3, 6, 2, 7, 8, 5]  # Example list
count = {}  # Dictionary to store counts of each number
duplicates = []  # List to store duplicate values

# Count occurrences of each number in the list
for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

# Find and collect duplicate values
for num, freq in count.items():
    if freq > 1:
        duplicates.append(num)

# Display duplicate values
print("Duplicate values are:", duplicates)

"""
ANSWER=
Duplicate values are: [2, 3, 5]
"""
