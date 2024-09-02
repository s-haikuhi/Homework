# 7. Lesson
"""
1. Arrange.
Arrange string characters such that lowercase letters should come first
Sample Input                Sample Output
PyNaTive                    yaivePNT
"""

# 1. SOLUTION

# Case 1.

target_word = 'PyNaTive'
uppercases = ''
lowercases = ''

for n in target_word:
    if n.isupper():
        uppercases += n
    elif n.islower():
        lowercases += n
print(f'{lowercases}{uppercases}')

# Output: yaivePNT

# Case 2.

target_word = 'PyNaTive'
uppercases = ''
lowercases = ''

for n in target_word:
    if n.isupper():
        uppercases += n
    elif n.islower():
        lowercases += n
print("".join([lowercases, uppercases]))

# Output: yaivePNT
