# Lesson 11. Functions

# Ex.1. Max of Three
"""
Write a Python function to find the Max of three numbers:
max_of_three(5, 11, 3).
Result: 11
"""


def max_of_three(given_list: list) -> list:
    max_value = given_list[0]
    for i in given_list:
        if i > max_value:
            max_value = i
    return max_value


print(max_of_three([5, 11, 3]))

# Output: 11


# Case 2

def max_num(given_list: list) -> int:
    given_list.sort(reverse=True)
    return given_list[0]


print(max_num([5, 11, 3]))

# Output: 11
