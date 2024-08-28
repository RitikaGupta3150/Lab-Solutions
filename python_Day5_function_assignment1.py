# Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(a, b):
    # Check if the divisor is not zero to avoid division by zero error
    if b == 0:
        return "Division by zero is undefined."
    else:
        return a / b

#asking user to enter 2 number to apply division
x=float(input("enter first number : "))
y=float(input("rnter the second number : "))
# Call the function with two numbers and print the result
result = div(x,y)
#print statement
print("The result of division is:", result)

"""
ANWER=
enter first number : 10
rnter the second number : 2
The result of division is: 5.0
"""
