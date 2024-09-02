# Lesson 5.
"""
Exercise 5: Sum of Squares Function
Write a function that calculates the sum of squares of numbers from 1 to n.
"""


def sum_squares(given_number: int) -> int:
    i = 1
    total_sum_squares = 0
    while i <= given_number:
        total_sum_squares += i ** 2
        i += 1
    return total_sum_squares


print(sum_squares(4))
# Output: 30
