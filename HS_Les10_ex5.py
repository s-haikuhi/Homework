# Lesson 10: While Loop Exercises
"""
Exercise 5:
Write a Python program that calculates the Fibonacci sequence up to a given number n
using a while loop. The Fibonacci sequence is a series of numbers where each number
is the sum of the two preceding ones.
"""
# a piece of Fibonacci Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...]

given_num = int(input("Positive Number = "))
fibonacci_sequence = [0]
sequence_item = 1
sum_sequence_items = fibonacci_sequence[0]
helper = 0


while given_num > (fibonacci_sequence[-1] + fibonacci_sequence[-helper]):
    if len(fibonacci_sequence) == 1:
        sequence_item += fibonacci_sequence[0]
        fibonacci_sequence.append(sequence_item)
        sum_sequence_items += sequence_item
        helper += 2
    else:
        sequence_item = fibonacci_sequence[- 1] + fibonacci_sequence[- 2]
        fibonacci_sequence.append(sequence_item)
        sum_sequence_items += sequence_item
print(f'Fibonacci sequence list up to a given number: {fibonacci_sequence}')
print(sum_sequence_items)

# Output for the user input 10: Fibonacci sequence list up to a given number: [0, 1, 1, 2, 3, 5, 8]
"""
20
"""
