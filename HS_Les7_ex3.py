# 7. Lesson
"""
3.Balance
Write a program to check if two strings are balanced. For example, strings s1 and
s2 are balanced if all the characters in the s1 are present in s2. The character’s
position doesn’t matter.
Sample Input            Sample Output
s1 = "Yn"               True
s2 = "PYnative"

s1 = "Ynf"              False
s2 = "PYnative"
"""

# 3. SOLUTION

#  Case 1.

s1 = 'Yn'
s2 = 'PYnative'

is_balanced = False

for i in s1:
    if i in s2:
        is_balanced = True
    else:
        is_balanced = False
print(is_balanced)

# Output: True


# Case 2.

s1 = 'Ynf'
s2 = 'PYnative'

is_balanced = False

for i in s1:
    if i in s2:
        is_balanced = True
    else:
        is_balanced = False
print(is_balanced)

# Output: False
