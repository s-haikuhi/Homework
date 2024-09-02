# Lesson 10: While Loop Exercises
"""
Exercise 1:
Write a Python program that prompts the user to enter a positive integer and then prints
all the numbers from 1 to that number using a while loop.
"""
positive_num = int(input("Fill in positive number only: "))
n = 1

if positive_num > 0:
    while n < positive_num:
        print(n)
        n += 1
else:
    while positive_num <= 0:
        positive_num = int(input("Fill in positive number only: "))
        while n < positive_num:
            print(n)
            n += 1
            
# Output for the user inputs [ -5, -4, 5] accordingly:
"""
Fill in positive number only: -5
Fill in positive number only: -4 
Fill in positive number only: 5
1
2
3
4
"""

# Case 2.

positive_num = int(input("Fill in positive number only: "))
start = 1

while positive_num <= 0:
    positive_num = int(input("Fill in positive number only: "))

if positive_num > 0:
    for i in range(start, positive_num):
        print(i)

# Output for the user inputs [ -5, -4, 5] accordingly:
"""
Fill in positive number only: -5
Fill in positive number only: -4 
Fill in positive number only: 5
1
2
3
4
"""