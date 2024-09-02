# Lesson 3: STRINGS
"""
3. Write a Python program to remove the n-th index character from a nonempty string.
Example:
Sample string: ‘abcdefgh’
n - 3
Expected result: abcefgh
"""

# 3. SOLUTION

new_word = 'Mondays'
n = 6
if 0 < len(new_word) > n:
    print(new_word[: n] + new_word[(n + 1):])
else:
    print('Not actual!')

# Output: Monday





