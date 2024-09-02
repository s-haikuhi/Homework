# Lesson 12
"""
Exercise 1: Check Pangram Function
Write a function that checks if a sentence is a pangram.

'The quick brown fox jumps over the lazy dog'
"""


def is_pangram(given_expression: str) -> bool:
    alpha_helper = "abcdefghijklmnopqrstuvwxyz"
    for i in alpha_helper:
        if i not in given_expression:
            return False
    return True


print(is_pangram('The quick brown fox jumps over the lay dog'))
# Output: False

print(is_pangram('The quick brown fox jumps over the lazy dog'))
# Output: True
