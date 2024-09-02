# Lesson 11.
"""
3.Factorial
Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument: factorial(5)
Result:
120
"""


def factorial(number: int) -> int:
    i = 1
    calculate_fact = 1

    while i <= number:
        calculate_fact *= i
        i += 1
    return calculate_fact


print(factorial(5))

# Output: 120


# Case 2

def factorial_given_n(number: int) -> int:
    calculate_factorial = 1
    for i in range(1, number + 1):
        calculate_factorial *= i
    return calculate_factorial


print(factorial_given_n(6))

# Output: 720
