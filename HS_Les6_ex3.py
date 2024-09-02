# 6. LESSON
"""
Exercise 3: Word Finder
Write a program that takes a list of words and a target word as input. The
program should find and print all words in the list that contain the target word.
Use a for loop, the in operator, and an if statement to check if the target word is
present in each word in the list.
"""
# 3. SOLUTION

# Case 1.

mixed_words = ['books for library', 'science', 'formula', 'information', 'degree', 'conformation', 'stage']
target_word = 'for'

for i in mixed_words:
    if target_word in i:
        print(i)

# Output:
"""
books for library
formula
information
conformation
"""

# Case 2.

mixed_words = ['books for library', 'science', 'formula', 'information', 'degree', 'conformation', 'stage']
target_word = 'for'

for i in mixed_words:
    if i.find(target_word) != -1:
        print(i)

# Output:
"""
books for library
formula
information
conformation
"""
