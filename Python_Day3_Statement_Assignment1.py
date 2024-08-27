#Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

#asking user for a number input
a=int(input("Enter a Number to Check:"))
#using a ternary operator to check if number is even or odd
if a % 2 == 0:
#print statement if number is even
    print("Number is even")
#print statemnet if number is odd
else:
    print("Number is odd")

"""
ANSWER =
Enter a Number to Check:5
Number is odd

Enter a Number to Check:426
Number is even
"""

