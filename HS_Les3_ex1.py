# Lesson 3: STRINGS
"""
1. Write a Python program to get a string made of the first 2 and the last 2 chars from a
given string.
Example:
Sample String : 'w3resource'
Expected Result : 'w3ce'
__________________________
Sample String : 'w3'
Expected Result : 'w3w3'
"""
# 1. SOLUTION

#  CASE 1.
emp_name = 'Aleksandr Ter-Melikyan'
print(emp_name[:2] + emp_name[-2:])

# Output: Alan

# CASE 2.

emp_name = 'Si'

if len(emp_name) == 2:
    print((emp_name[:2] * 2))
else:
    print(emp_name[:2] + emp_name[-2:])

# Output: SiSi
