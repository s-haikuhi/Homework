# Lesson 10: While Loop Exercises
"""
Exercise 4:
Write a Python program that generates a random number between 1 and 100 and asks
the user to guess the number. The program should give hints whether the guessed
number is too high or too low until the correct number is guessed.
"""
# Case 1.Too helpful hint to guess the number

import random

random_number = random.randint(1, 100)
print(f'The Random Number is {random_number}')
guess_number = int(input("Guess the Number in [1 - 100] range: "))

while guess_number <= 100:
    if guess_number - random_number > 0:
        guess_number = int(input(f'Your number is higher from the target by {guess_number - random_number}: '))
    elif guess_number - random_number < 0:
        guess_number = int(input(f'Your number is smaller from the target by {random_number - guess_number}: '))
    else:
        print("You are the Winner")
        break

# Output: You are the Winner

# Case 2.

random_number = random.randint(1, 100)
print(f'The Random Number is {random_number}')
guess_number = int(input("Guess the Number in [1 - 100] range: "))

while guess_number <= 100:
    while guess_number - random_number > 0:
        guess_number = int(input(f'Your number is greater: guess the number in the range from '
                                 f'[{random_number - 2} to {guess_number - 1}]: '))
    while guess_number - random_number < 0:
        guess_number = int(input(f'Your number is smaller: guess the number in the range from '
                                 f'[{guess_number + 1} to {random_number + 2}]: '))
    if guess_number == random_number:
        print("You are the Winner")
        break

# Output: You are the Winner

# Case 3.
random_number = random.randint(1, 100)
print(f'The Random Number is {random_number}')
guess_number = int(input("Guess the Number in [1 - 100] range: "))

while guess_number != random_number:
    while guess_number < random_number:
        guess_number = int(input(f'Your number is smaller. Please, try again: '))
    while guess_number > random_number:
        guess_number = int(input(f'Your number is greater. Please, try again: '))
else:
    print("You are the Winner")

# Output: "You are the Winner"
