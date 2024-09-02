# 4. LESSON: ARITHMETIC OPERATIONS
"""
3.Digit Sum:
Input a two-digit natural number and output the sum of its digits. You can
assume that the input will be a two-digit number and need not check that
programmatically.
Sample Input    Sample Output
15              6
78              15
20              2
"""
# 3. SOLUTION

nat_num = int(input('Natural Number N = '))

if 10 <= nat_num < 100:
    print(nat_num//10 + nat_num % 10)
else:
    print('Two-digit natural number is accepted only.')

# Output for the user inputs [15, 78 20] accordingly:
"""
6
15
2
"""


# Other Solution

nat_num = int(input('Natural number = '))
print(int(str(nat_num)[0]) + int(str(nat_num)[-1]))

# Output for the user inputs [ 15, 78, 20 ] accordingly:
"""
6
15
2
"""

