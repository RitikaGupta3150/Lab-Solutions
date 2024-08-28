#Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number

def square(n):
    # Return the square of the given number
    return n * n
#asking user ro enter a number
a=float(input("Enter a number to square it : "))
# Call the function with a number and print the result
result = square(a)
print("The square of the number is:", result)

"""
ANSWER=
Enter a number to square it : 45
The square of the number is: 2025.0
"""
