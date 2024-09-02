"""1. Write a Python program to count the occurrences of each word in a given sentence 

string = “To change the overall look of your document. To change the look available in the gallery”
"""

from collections import Counter
import re

# Given string
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Normalize the sentence by converting it to lowercase and removing punctuation
normalized_sentence = re.sub(r'[^\w\s]', '', sentence).lower()

# Split the sentence into words
words = normalized_sentence.split()

# Count the occurrences of each word
word_count = Counter(words)

# Print the word counts
print("Word Counts:", word_count)


"""
ANSWER=
Word Counts: Counter({'the': 3, 'to': 2, 'change': 2, 'look': 2, 'overall': 1, 'of': 1, 'your': 1, 'document': 1, 'available': 1, 'in': 1, 'gallery': 1})
"""
