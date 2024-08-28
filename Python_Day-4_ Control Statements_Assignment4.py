# Create a Python program that checks if a user-given number is positive, negative, or zero.

#asking user to enter an integer
A=int(input("Enter a Integer : "))
#using nested if statement to determine if a user-given number is positive, negative, or zero.
#using if statement to check if number is positive(greater than 0)
if A>0:
    print(f"{A} is Positive")
#using elif statement to check if number is negative(less than 0)
elif A<0:
    print(f"{A} is Negative")
#using else statement to check if number is equal to 0
else:
    print(f"{A} is Zero")

"""
ANSWER=
Enter a Integer : 5
5 is Positive

Enter a Integer : -8
-8 is Negative

Enter a Integer : 0
0 is Zero
"""
