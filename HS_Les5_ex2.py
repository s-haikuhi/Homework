# 5. LESSON
"""
2.Largest:
Write a Python program to get the largest number from a list.
Sample Input                Sample Output
[1, 2, 3, 4]                4
[5, 7, 3, 9, 11]            11
[25, 1,1, 13]               25
[1, 2, 1, 1]                2
"""
# 2. SOLUTION

target_list = [1, 2, 3, 4]
largest_i = target_list[0]

for i in target_list[1:]:
    if i >= largest_i:
        largest_i = i
print(largest_i)

# Output: 4

# Other Solution

# Case 1.
target_list = [1, 2, 3, 4]
target_list.sort(reverse=True)
print(target_list[0])
# Output: 4

# Case 2.
target_list = [5, 7, 3, 9, 11]
target_list.sort()
print(target_list[-1])

# Output: 11
