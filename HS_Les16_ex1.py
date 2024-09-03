# Lesson 16.
"""
1. String Length Checker
Write a function that checks the length of a string provided by the user. Handle the
TypeError by raising a custom exception if the input is not a string.
"""
import string

check_length = lambda txt: len(txt)
user_input = input()

for i in user_input:
    if i not in string.ascii_letters:
        raise TypeError("Only strings are allowed.")
    else:
        check_length(user_input)

print(check_length(user_input))

# Output for the inputs ["encourage", "go4adventures"] accordingly:
"""
9
TypeError: Only strings are allowed.
"""

check_length = lambda txt: len(txt)
provided_input = "leadership"


try:
    check_length(provided_input)
except TypeError as te:
    raise TypeError("Only strings are allowed.")

print(check_length(provided_input))

# Output for the inputs [1456, "leadership"] accordingly:
"""
TypeError: Only strings are allowed.
10
"""
