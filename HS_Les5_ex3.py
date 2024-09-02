# 5. LESSON
"""
3.Smallest:
Write a Python program to get the smallest number from a list.
Sample Input            Sample Output
[1, 2, 3, 4]            1
[5, 7, 3, 9, 11]        3
[25, 1,1, 13]           1
[1, 2, 1, 1]            1
"""
# 3. SOLUTION

target_list = [1, 2, 3, 4]
smallest_i = target_list[0]

for i in target_list[1:]:
    if i <= smallest_i:
        smallest_i = i
print(smallest_i)

# Output: 1

