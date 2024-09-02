# 6. LESSON
"""
Exercise 1: Counting Even Numbers
Write a program that takes a list of numbers as input and counts the number of
even numbers in the list.
Use a for loop, an if statement, and the modulus
operator (%) to determine if a number is even or odd.
"""
# 1. SOLUTION

# Case 1.

target_list = [1, 3, 5, 7, 2, 4, 6, 8, 9, 11, 13, 14, 15, 17, 16, 18, 21, 22]
quantity_evens = 0

for n in target_list:
    if n % 2 == 0:
        quantity_evens += 1
print(quantity_evens)

# Output: 8
