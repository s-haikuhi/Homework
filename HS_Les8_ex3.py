# Lesson 8. Sets
"""
Exercise 3:
Write a Python function that takes two sets as input and returns a new set containing
elements that are present in the first set but not in the second set.
"""
org_structure1 = {'Founder office', 'Deputy CEO office', 'Directorate', 'Department', 'Unit'}
org_structure2 = {'Directorate', 'Department', 'Unit', 'Subunit', 'Team', 'Group'}

target_list = org_structure1 - org_structure2
print(target_list)

# Output: { 'Founder office', 'Deputy CEO office'}
# Note that the order of the output is not stable
