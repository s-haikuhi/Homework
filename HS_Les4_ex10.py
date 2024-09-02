# 4. LESSON: ARITHMETIC OPERATIONS
"""
10.Salaries:
Given the salaries of three employees working at a department, find the
amount of money by which the salary of the highest-paid employee differs
from the salary of the lowest-paid employee. The input consists of three
positive integers - the salaries of the employees. Output a single number,
the difference between the top and the bottom salaries
Sample Input            Sample Output
100 500 1000            900
500 100 1000            900
36 11 20                25
20 20 20                0
"""
# 10. SOLUTION

# Case 1.

Emp1 = int(input("Salary: "))
Emp2 = int(input("Salary: "))
Emp3 = int(input("Salary: "))

if Emp1 > 0 < Emp2 and Emp3 > 0:
    if Emp1 <= Emp2 <= Emp3:
        print(Emp3 - Emp1)
    elif Emp3 <= Emp2 <= Emp1:
        print(Emp1 - Emp3)
    elif Emp2 <= Emp1 <= Emp3:
        print(Emp3 - Emp2)
    elif Emp3 <= Emp1 <= Emp2:
        print(Emp2 - Emp3)
    elif Emp2 <= Emp3 <= Emp1:
        print(Emp1 - Emp2)
    elif Emp1 <= Emp3 <= Emp2:
        print(Emp2 - Emp1)
else:
    print("Salary amount to be presented in positive number")

# Output for the user inputs [100 500 1000, 500 100 1000, 36 11 20, 20 20 20] accordingly:
"""
900
900
25
0
"""

# Other Solution

# Case 1.
Salary1 = int(input('1. Amount of Salary: '))
Salary2 = int(input('2. Amount of Salary: '))
Salary3 = int(input('3. Amount of Salary: '))

Salaries = [Salary1, Salary2, Salary3]
highest_sal = Salaries[0]
lowest_sal = Salaries[0]

if Salary1 > 0 < Salary2 and Salary3 > 0:
    for n in Salaries[1:]:
        if n > highest_sal >= lowest_sal:
            highest_sal = n
        elif n < lowest_sal <= highest_sal:
            lowest_sal = n
    print(highest_sal - lowest_sal)
else:
    print("Salary amount to be presented in positive number")

# Output for the user inputs [100 500 1000, 500 100 1000, 36 11 20, 20 20 20] accordingly:
"""
900
900
25
0
"""

# Case 2

Salary1 = int(input('1. Amount of Salary: '))
Salary2 = int(input('2. Amount of Salary: '))
Salary3 = int(input('3. Amount of Salary: '))

Salaries = [Salary1, Salary2, Salary3]

if Salary1 > 0 < Salary2 and Salary3 > 0:
    Salaries.sort()
    print(Salaries)
    print(Salaries[-1] - Salaries[0])
else:
    print("Salary amount to be presented in positive number")

# Output for the user inputs [100 500 1000, 500 100 1000, 36 11 20, 20 20 20] accordingly:
"""
900
900
25
0
"""
