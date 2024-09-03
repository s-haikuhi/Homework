# Lesson 13.
"""
4. Write a Python program to find intersection of two given arrays using
Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]
"""
# Case 1.

intersection = list(filter(lambda n: n in [1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]))

print(intersection)
# Output: [1, 2, 8, 9]


# Case 2.

intersection_of_two = lambda array1, array2: array1 & array2

print(list(intersection_of_two({1, 2, 3, 5, 7, 8, 9, 10}, {1, 2, 4, 8, 9})))
# Output: [8, 1, 2, 9]
