# Lesson 3: STRINGS
"""
8. Create a string made of the first, middle and last character of given string with odd number of
symbols․
Example:
Sample = ‘Sevak’
Expected ‘Svk’
"""

# 8. SOLUTION

# Case 1.

course = 'statistic'
middle_index = int(len(course) / 2)

Rename_course = course[0] + course[middle_index] + course[-1]
print(Rename_course)

# Output:  sic


# Case 2.

course = 'statistics'
middle_index = int(len(course) / 2)

if len(course) % 2 != 0:
    print(course[0] + course[middle_index] + course[-1])
else:
    print("Not actual!")

# Output:  Not actual!
