# Lesson 9.
"""
Exercise 1:
Print the even numbers from 0 to 20 using a for loop and the range function
"""
# 1. Solution
start = 0
stop = 21
step = 2

for i in range(start + 2, stop, step):
    print(i)

# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

# case
for i in range(2, 21, 2):
    print(i)

# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
