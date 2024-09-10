#2. Write a Python program to get the largest and smallest number from a list without builtin functions.

# Python program to find the largest and smallest number from a list

numbers = [10, 20, 5, 45, 99, 2]  # Example list

# Initialize largest and smallest variables with the first element of the list
largest = numbers[0]
smallest = numbers[0]

# Loop through each number in the list
for num in numbers:
    if num > largest:
        largest = num  # Update largest if a bigger number is found
    if num < smallest:
        smallest = num  # Update smallest if a smaller number is found

# Display the largest and smallest numbers
print("The largest number is:", largest)
print("The smallest number is:", smallest)

"""
ANSWER=
The largest number is: 99
The smallest number is: 2
"""
