# 4. LESSON: ARITHMETIC OPERATIONS
"""
6.Comparison։
Input two positive integers, and output a line describing their relation.
Follow the sample format.
Sample Input            Sample Output
7 9                     7 < 9
11 11                   11 = 11
4 -4                    4 > -4
"""

num1 = int(input('First Number = '))
num2 = int(input('Second Number = '))


if num1 > 0 < num2:
    if num1 < num2:
        print(str(num1) + ' < ' + str(num2))
    elif num2 < num1:
        print(str(num1) + ' > ' + str(num2))
    elif int(num1) == int(num2):
        print(str(num1) + ' = ' + str(num2))
else:
    print('Positive integers are accepted only')

# Output for the user inputs [ 7 9], [11 11], [4 -4] accordingly:
"""
7 < 9
11 = 11
'Positive integers are accepted only'
"""
