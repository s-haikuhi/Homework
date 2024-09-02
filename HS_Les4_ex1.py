# 4. LESSON: ARITHMETIC OPERATIONS
"""
1. SUM:
Input two integers and print out their sum. Preserve the exact format from
the examples (e.g. the output should contain exactly three lines)
Sample Input        Sample Output
4 5                 а = 4
                    b = 5
                    a + b = 4 + 5 = 9

17 8                a = 17
                    b = 8
                    a + b = 17 + 8 = 25
"""
# 1.SOLUTION

# Case 1.

a = input('a = ')
b = input('b = ')
total = int(a) + int(b)

print('a + b = ' + a + ' + ' + b + ' = ' + str(total))
# Output for the user inputs 4 and 5:
"""
a = 4
b = 5
a + b = 4 + 5 = 9
"""

# Case 2.
workers = input('workers = ')
staff = input('staff = ')
emp_num = int(staff) + int(workers)

print('workers + staff = ' + workers + ' + ' + staff + ' = ' + str(emp_num))

# Output for the user inputs 17 and 8:
"""
workers = 17
staff = 8
workers + staff = 17 + 8 = 25
"""

# Case 3

male = int(input("number of male: "))
female = int(input("number of female: "))
total_empl = male + female
print(f"male = {male} \nfemale = {female} \nmale + female = {male} + {female} = {total_empl}")

# Output for the user inputs 17 and 8:
"""
male = 17
female = 8
male + female = 17 + 8 = 25
"""
