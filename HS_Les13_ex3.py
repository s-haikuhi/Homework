# Lesson 13.
"""
3. Write a Python program to check whether a given string is number or
not using Lambda.
"""

is_number = lambda given_str: given_str.isnumeric()             # or .isdigit()
print(is_number("1a"))
# Output: False

print(is_number("10"))
# Output: True

