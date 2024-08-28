# Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

#asking user to enter their age
Age=int(input("Enter your age : "))
#using if statement to check if the age entered is eligible to vote or not
if Age>=18:
#print statement if the condition is true
    print("You are eligible to vote!")
else:
#print statemnet if condition is false
    print("You are not eligible to vote!")

"""
Enter your age : 20
You are eligible to vote!

Enter your age : 15
You are not eligible to vote!

"""

