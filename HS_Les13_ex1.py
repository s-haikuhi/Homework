# Lesson 13.
"""
Ex. 1. Write a Python program to square and cube every number in a given list of
integers using Lambda.
Sample. ([1,2,3,4,5])
Output: ([1, 4, 9, 16, 25], [1, 8, 27, 64, 125])
"""
# 1. Solution

# Case 1.

given_list = ([1, 2, 3, 4, 5])
squares_res = map(lambda n: n ** 2, given_list)
cubes_res = map(lambda n: n ** 3, given_list)
print((list(squares_res), list(cubes_res)))

# Output: ([1, 4, 9, 16, 25], [1, 8, 27, 64, 125])


# Other case: to square and cube at the same time

print(list(map(lambda n: (n ** 2) ** 3, [1, 2, 3, 4, 5])))

# Output: [1, 64, 729, 4096, 15625]
