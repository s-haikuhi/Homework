# Lesson 3: STRINGS
"""
7. Write a Python program to print the floating numbers upto 2 decimal places
(number must be not greater than 10)
Example:
Sample = 2.145548
Expected - 2.14
_______________________
Sample = 9.5748
Expected - 9.57
"""

# 7. SOLUTION

# Case 1.

price = 5.123456

if price < 10:
    print(str(price)[:4])
else:
    print("The number should be less than 10.")

# Output: 5.12

# Case 2.

price = 2500055.143456
num_char = 2
new_price = str(price)
print(new_price[:(new_price.find('.') + 1 + num_char)])

# Output: 2500055.14

