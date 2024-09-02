# Lesson 8. Sets
"""
Exercise 4:
Write a Python function that takes two sets as input and returns a new set containing
elements that are present in either of the input sets, but not in both.
"""
Month1 = {"January", "February", "November", "October", 'December'}
Month2 = {"March", "April", "May", "June", "November", "October"}
target_month = Month1 ^ Month2
print(target_month)

# Output: {"December", "January", "February", "March", "April", "May", "June"}
# Note that the order of the output is not stable
