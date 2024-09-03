# Lesson 13.
"""
Write a Python program to add two given lists using map and lambda.

Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]
"""
addition_of_two = list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))

print(addition_of_two)
# Output: [5, 7, 9]
