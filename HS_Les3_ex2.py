# Lesson 3: STRINGS
"""
2. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string
is less than 3, leave it unchanged.

Example:
Sample String : 'abc'
Expected Result : 'abcing'
_______________________
Sample String : 'string'
Expected Result : 'stringly'
"""

# 2. SOLUTION

# Case 1.

given_expression = 'breath'         # try other inputs: "fly", "according", "we"

if len(given_expression) >= 3:
    if given_expression[-3:] != 'ing':
        print(given_expression + 'ing')
    else:
        print(given_expression + 'ly')
else:
    print(given_expression)


# Output for the inputs  "breath", "fly", "according", "we" accordingly:
"""
breathing
flying
accordingly
we
"""


# Case 2.
m_goal = ["breath", "fly", "according", "we"]

for i in m_goal:
    if len(i) >= 3:
        if not i.endswith('ing'):
            print(i + 'ing')
        else:
            print(i + 'ly')
    else:
        print(i)

# Output for the inputs  "breath", "fly", "according", "we" accordingly:
"""
breathing
flying
accordingly
we
"""

