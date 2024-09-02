# Lesson 3: STRINGS
"""
5. Write a Python function to get a string made of 4 copies of the last two characters of a
specified string (length must be at least 2).
Sample = ‘Python'
Expected onononon
________________
Sample 'Exercises'
Expected eseseses
"""

# 5. SOLUTION

requirement = 'proficiency'
num_copy = 4
char_to_copy = 2
copied_v = requirement[-char_to_copy:] * num_copy
print(copied_v)

# Output: cycycycy
