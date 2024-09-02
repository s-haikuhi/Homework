# 4. LESSON: ARITHMETIC OPERATIONS
"""
11.Rounding - 2:
Given a real number, round it to the nearest whole.
Sample Input        Sample Output
0.3                 0
1.2398              1
1.5                 2
67.567              68
"""

# 11. SOLUTION

real_num = float(input('Real number = '))

if real_num - int(real_num) >= 0.5:
    print(int(real_num) + 1)
else:
    print(int(real_num))

# Output for the user inputs [0.3, 1.2398, 1.5, 67.567] accordingly:
"""
0
1
2
68
"""

# Other solution

real_num = float(input('Real number = '))
print(round(real_num))

# Output for the user inputs [0.3, 1.2398, 1.5, 67.567] accordingly:
"""
0
1
2
68
"""

