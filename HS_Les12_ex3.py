# Lesson 12
"""
Exercise 3: Average Function
Write a function that calculates the average of a list of numbers.
"""


def get_average_of_list_nums(given_list: list) -> float:
    average_numbers = 0
    sum_numbers = 0
    for i in given_list:
        sum_numbers += i
    return sum_numbers / len(given_list)


print(get_average_of_list_nums([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))

# Output: 55.0
