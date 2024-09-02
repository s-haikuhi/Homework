# Lesson 8. Sets
"""
Exercise 2:
Write a Python function that takes two sets as input and returns a new set containing all
unique elements from both input sets.
"""
Marketing_salary = {1000, 1200, 1300, 1500, 1800}   # USD
It_salary = {1500, 1800, 2500, 3500, 4500, 5000}    # USD

target_salary = Marketing_salary ^ It_salary
print(target_salary)

# Output: {1000, 1200, 1300, 2500, 3500, 4500, 5000}
# Note that the order of the output is not stable
