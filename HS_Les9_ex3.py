# Lesson 9.
"""
Exercise 3:
Print a right-angled triangle pattern using a nested for loop. The pattern should have 5
rows.
"""
# Solution

pattern1 = "*"
pattern2 = " "

for i in range(1, 6):
    for j in pattern2:
        print((pattern1 + pattern2) * i)

# Output:
"""
*
* *
* * *
* * * *
* * * * *
"""

# Case 2. Without nested loop

pattern = "* "
start = 1
stop = 6

for i in range(start, stop):
    print(i * pattern)

# Output
"""
*
* *
* * *
* * * *
* * * * *
"""

# Other: Christmas tree

pattern1 = "*"
pattern2 = " "
helper = 4
for i in range(1, 6):
    for j in pattern2:
        print(pattern2 * helper + (pattern1 + pattern2) * i)
        helper -= 1

# Output:
"""
    *
   * *
  * * *
 * * * *
* * * * *

"""