#2. Write a python program finding the factorial of a given number using a while loop

def factorial(number):
   
    # Ensure the number is non-negative
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Initialize the result to 1 (the factorial of 0 is 1)
    result = 1
    
    # Initialize a counter to multiply with the result
    current = 1
    
    # Calculate the factorial using a while loop
    while current <= number:
        result *= current  # Multiply result by the current number
        current += 1       # Increment the counter
    
    return result

# Prompt the user to enter a number
num = int(input("Enter a non-negative integer: "))

# Call the factorial function and display the result
try:
    print(f"The factorial of {num} is {factorial(num)}.")
except ValueError as e:
    print(e)
    
"""
ANSWER=
Enter a non-negative integer: 5
The factorial of 5 is 120.
"""
