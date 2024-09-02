# Lesson 9.
"""
Exercise 4:
Print the multiplication table of 5 using a for loop and f”strings”.
The table should be printed up to 10.
"""
to_multiply = 5
start = 1
stop = 11

for n in range(start, stop):
    print(f'{to_multiply} * {n} = {n * to_multiply}')

# Output
"""
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
"""