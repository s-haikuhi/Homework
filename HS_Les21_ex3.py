# Lesson 21
"""
3. List Exercise:
Given a list of numbers, write a function to find the sum of all numbers in the list that
can be divided by 7.
"""

# Case 1
given_list = [1, 5, 10, 14, 20, 21, 24, 26, 28, 30, 35, 42, 48, 50, 55, 63, 70, 77, 90, 92]


def sum_of_numbers_divided_7(target_list: list):
    sum_numbers_divided_7 = 0
    for i in target_list:
        if i % 7 == 0:
            sum_numbers_divided_7 += i
    return sum_numbers_divided_7


print(sum_of_numbers_divided_7(given_list))
# Output for the given list: 350


# Case 2: with range

def sum_divided_7(target):
    step = 7
    sum_of_7th_divided = 0
    target_range = range(0, target + 1, step)
    for i in target_range:
        sum_of_7th_divided += i
    return sum_of_7th_divided


print(sum_divided_7(92))
# Output: 637


# Case 3
given_list = [1, 5, 10, 14, 20, 21, 24, 26, 28, 30, 35, 42, 48, 50, 55, 63, 70, 77, 90, 92]

sum_numbers_div_7 = list(filter(lambda n: n % 7 == 0, given_list))
total_sum = 0

for i in sum_numbers_div_7:
    total_sum += i
print(total_sum)

# Output: 350
