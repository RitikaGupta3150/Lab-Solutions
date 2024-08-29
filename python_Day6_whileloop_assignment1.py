#1.Write a python program to check whether a number is palindrome or not?
def is_palindrome(number):
    
    # Convert the number to a string
    str_number = str(number)
    
    # Create the reversed version of the string
    reversed_str = str_number[::-1]
    
    # Check if the original string is equal to the reversed string
    return str_number == reversed_str

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Call the is_palindrome function and store the result
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


"""
ANSWER=
Enter a number: 123454321
123454321 is a palindrome.
"""
