# 4. LESSON: ARITHMETIC OPERATIONS
"""
8.Three Numbers
Input three integers. Output the word “Sorted” if the numbers are listed
in increasing or decreasing order and "Unsorted" otherwise
Sample Input                Sample Output
1 2 3                       Sorted
1 3 2                       Unsorted
5 0 -4                      Sorted
9 9 9                       Sorted
9 9 0                       Sorted
"""
# 8. Solution

num1 = int(input('First Number = '))
num2 = int(input('Second Number = '))
num3 = int(input('Third Number = '))
print(num1, num2, num3)

if num1 <= num2 <= num3 or num1 >= num2 >= num3:
    print('Sorted')
else:
    print('Unsorted')

# Output for the user inputs [1 2 3, 1 3 2, 5 0 -4, 9 9 9, 9 9 0] accordingly:
"""
Sorted
Unsorted
Sorted
Sorted
Sorted
"""
