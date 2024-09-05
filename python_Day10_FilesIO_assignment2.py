#Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words(filename):
    try:
        # Open the file in read mode
        file = open(filename, 'r')
        
        # Read the entire file content
        content = file.read()
        
        # Split the content into words
        words = content.split()
        
        # Count the number of words
        word_count = len(words)
        
        # Display the total number of words
        print("Total number of words:", word_count)
        
        # Close the file
        file.close()
    
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
count_words(r"C:\Users\asus\Downloads\ABC.txt")

"""
ANSWER=
Total number of words: 136
"""
