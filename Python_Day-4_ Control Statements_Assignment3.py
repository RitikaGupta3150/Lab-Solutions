#Write a Python program that determines if a given year is a leap year or not.

#asking user to enter a year
Year=int(input("Enter the year: "))
#using if statement to check if the year entered is a leap year or not
if Year%4 ==0 :
#print statement if the condition is true 
    print(f"{Year} is a leap year")
else:
#print statement if the condition is false 
    print(f"{Year} is not a leap year")
    

"""
ANSWER=
Enter the year: 2020
2020 is a leap year

Enter the year: 2021
2021 is not a leap year
"""
