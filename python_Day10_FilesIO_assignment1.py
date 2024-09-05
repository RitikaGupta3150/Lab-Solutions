#. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_file(filename):
    # Open the file in read mode
    file = open(filename, 'r')
    
    # Read and print each line
    for line in file:
        print(line, end='')  # Print the line without adding extra newlines
    
    # Close the file
    file.close()

# Example usage
read_file(r"C:\Users\asus\Downloads\ABC.txt")


"""
ANSWER=
In the world of mathematics and logic, every problem presents an opportunity to explore patterns, relationships, and strategies. Solving a problem, whether it's about combinations, permutations, or another concept, often reveals more than just an answerâ€”it uncovers a deeper understanding of how systems work.

For instance, when tackling a problem involving combinations, such as selecting balls from a box, youâ€™re not just performing calculations; youâ€™re analyzing the structure of the problem and using logical reasoning to arrive at the solution. Itâ€™s like piecing together a puzzle, where each piece of information helps build the bigger picture.

In the end, the beauty of mathematics lies not only in finding the correct answer but also in appreciating the process of discovery and the satisfaction that comes from solving complex problems. Keep exploring and enjoying the journey of learning!
"""
