# Lesson 15.
"""
1. Dice Rolling Simulator:
○ Develop a simple dice rolling simulator. Generate random numbers between 1 and 6 to
simulate the roll of a six-sided die using the random module.
"""
from random import randint

# Case 1.

dice_rolling_simulator = lambda x, y: randint(x, y)
print(int(dice_rolling_simulator(1, 6)))
