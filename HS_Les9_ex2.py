# Lesson 9.
"""
Exercise 2:
Print a square pattern using a nested for loop. The pattern should have 5 rows and 5
columns.
"""

# Solution

# Case 1.
pattern = "*"
start = 0
stop = 5
pattern_2 = " "
for i in range(start, stop):
    for n in pattern_2:
        print((pattern + pattern_2) * stop)

# Output:
"""
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""


# Case 2.
pattern = "* "
start = 0
stop = 5

for i in range(start, stop):
    print(pattern * stop)

# Output:
"""
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""

