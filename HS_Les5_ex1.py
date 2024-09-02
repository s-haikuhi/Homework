# 5. LESSON
"""
1.Multiply:
Write a Python program to multiply all the items in a list.
Sample Input            Sample Output
[1, 2, 3, 4]            24
[5, 7, 3, 9, 11]        10395
[25, 1,1, 13]           325
"""
# 1. SOLUTION

# Case 1.
target_list = [5, 7, 3, 9, 11]
multiplication_of_nums = 1

for n in target_list:
    multiplication_of_nums *= n
print(multiplication_of_nums)

# Output: 10395
