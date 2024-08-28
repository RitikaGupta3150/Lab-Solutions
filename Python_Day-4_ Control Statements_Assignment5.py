#Write a Python program that determines the largest of three numbers entered by the user.

#asking user to enter 3 numbers
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))
#creating a function to check the largest number amongst the 3 numbers entered
def find_largest(num1, num2, num3):
#if statement to check if num1 is largest
    if num1 >= num2 and num1 >= num3:
        return num1
#elif statement to check if num2 is largest
    elif num2 >= num1 and num2 >= num3:
        return num2
#else statement to return num3 largest if above statement are false
    else:
        return num3
#print statement to print the largest number
largest = find_largest(num1, num2, num3)
print(f"The largest of the three numbers is: {largest}")

"""
ANSWER=
Enter the 1st number:5
Enter the 2nd number:3
Enter the 3rd number:2
The largest of the three numbers is: 5

"""
