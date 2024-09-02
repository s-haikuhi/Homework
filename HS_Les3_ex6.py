# Lesson 3: STRINGS
"""
6. Write a Python function to get a string made of its first three characters of a specified string. If
the length of the string is less than 3 then return the original string.
Example:
Sample ='ipy'
Expected ipy
______________
Sample ='python'
Expected pyt
"""

# 6. SOLUTION

# Case 1.

requirement = 'proficiency'
main_char = 3

if len(requirement) >= 3:
    print(requirement[:main_char])
else:
    print(requirement)

# Output: pro



