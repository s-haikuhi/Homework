# 4. LESSON
"""
2.The Last Digit:
Input a natural number N and output its last digit.

Sample          Input Sample Output
156             6
789155          5
7               7
"""

# 2. SOLUTION

nat_num = int(input('Natural Number N = '))
if nat_num > 0:
    print(nat_num % 10)
else:
    print("Not actual!")

# Output for the user inputs [156, 789155, 7] accordingly:
"""
6
5
7
"""

# Other Solution

nat_num = int(input('Natural number = '))

if nat_num > 0:
    print(str(nat_num)[-1])
else:
    print('Not actual!')

# Output for the user inputs [156, 789155, 7] accordingly:
"""
6
5
7 
"""

# Case 2: when the user input is [ 0 ]
# output: Not actual!

# Case 3: when the user input is [ - 45 ]
# output: Not actual!

# Case 4: when the user input is [ 45.569 ]
# output: ValueError

# Case 5: when the user input is [ sonne ]
# output: ValueError
