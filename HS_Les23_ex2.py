# Lesson 23
"""
2. Character Frequency:
○ Given a string, create a dictionary where keys are characters and values are their
frequencies in the string.
"""
given_string = "eintrittskarte"

target_dict = {k: list(given_string).count(k) for k in given_string}
print(target_dict)

# Output
"""
{'e': 2, 'i': 2, 'n': 1, 't': 4, 'r': 2, 's': 1, 'k': 1, 'a': 1}
"""
