#Python program to check if a given number is an Armstrong number

def is_armstrong_number(number):
    # Convert number to string to easily iterate over digits
    num_str = str(number)
    # Get the number of digits
    num_digits = len(num_str)
    
    # Initialize sum of powers
    sum_of_powers = 0
    
    # Calculate the sum of each digit raised to the power of num_digits
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

# Test the function
test_number = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong_number(test_number):
    print(f"{test_number} is an Armstrong number.")
else:
    print(f"{test_number} is not an Armstrong number.")

"""
ANSWER=
Enter a number to check if it's an Armstrong number: 153
153 is an Armstrong number.

= RESTART: C:/Users/asus/OneDrive/Desktop/Ritika _DANLC/python_Day7_forloop_assignment2.py
Enter a number to check if it's an Armstrong number: 3150
3150 is not an Armstrong number.
"""
