# 5. LESSON
"""
5.Duplicates
Write a Python program to remove duplicates from a list.
Sample Input            Sample Output
[1, 2, 3, 1]            [1, 2, 3]
[5, 7, 3, 9, 11]        [5, 7, 3, 9, 11]
[25, 1,1, 13]           [25, 1, 13]
"""
# 5. SOLUTION

# Case 1.

target_list = [1, 2, 3, 1]

new_list = []

for i in target_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

# Output: [1, 2, 3]


# Case 2.

target_list = [1, 2, 3, 1]
print(list(set(target_list)))

# Output: [1, 2, 3]
