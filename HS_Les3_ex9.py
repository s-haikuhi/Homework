# Lesson 3: STRINGS
"""
9. Append new string in the middle of a given (even number of characters) string.
Sample = ‘python’
new_string = ‘new’
Expected ‘pytnewhon
"""

# 9. SOLUTION

course = 'Geromany'
element = 'neu'
if len(course) % 2 == 0:
    middle_index = int(len(course)/2)
    print(course[:middle_index] + element + course[middle_index:])
else:
    print("Not actual!")

# Output: Geroneumany
