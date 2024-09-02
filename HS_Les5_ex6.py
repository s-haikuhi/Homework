# 5. LESSON
"""
6.Square
Turn every item of a list into its square
Sample Input            Sample Output
[5, 7, 3, 9, 11]        [25, 49, 9, 81, 121]
"""
# 6. SOLUTION

# Case 1. Squares in a new list
target_list = [5, 7, 3, 9, 11]
new_list = []
n = 2

for i in target_list:
    new_list.append(i ** n)
print(new_list)

# Output: [25, 49, 9, 81, 121]

# Case 2.
target_list = [5, 7, 3, 9, 11]
n = 2
index = 0

for i in target_list:
    target_list[index] = i ** n
    index += 1
print(target_list)

# Output: [25, 49, 9, 81, 121]

