# Lesson 11. Functions
"""
2.Letters Count
Write a Python function to calculate count of each letter in string: count_letters(‘abrakadabra’)
Result:
{a: 5, b: 2, r: 2, k: 1, d: 1}
"""


def count_letters(given_expr: str) -> dict:
    target_dict = {}
    for i in given_expr:
        if i not in target_dict:
            target_dict[i] = 1
        else:
            target_dict[i] += 1
    return target_dict


print(count_letters('abrakadabra'))

# Output: {'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1}

