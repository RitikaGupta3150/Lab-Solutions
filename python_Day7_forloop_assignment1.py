#Python program to check if the given string is a palindrome

def is_palindrome(s):
    # Remove any spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    
    # Initialize start and end pointers
    start = 0
    end = len(s) - 1
    
    # Loop to compare characters from both ends
    for i in range(len(s) // 2):
        if s[start] != s[end]:
            return False  # Characters do not match, not a palindrome
        start += 1
        end -= 1
    
    return True  # All characters matched, it is a palindrome

# Test the function
test_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")

"""
ANSWER=
Enter a string to check if it's a palindrome: bob
'bob' is a palindrome.


Enter a string to check if it's a palindrome: ritika
'ritika' is not a palindrome.
"""
