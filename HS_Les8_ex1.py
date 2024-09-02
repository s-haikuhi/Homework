# Lesson 8. Sets
"""
Exercise 1:
Write a Python function that takes two sets as input and returns a new set containing
elements that are present in both input sets.
"""

org_structure1 = {'Founder office', 'Deputy CEO office', 'Directorate', 'Department', 'Unit'}
org_structure2 = {'Directorate', 'Department', 'Unit', 'Subunit', 'Team', 'Group'}

target_list = org_structure1 & org_structure2
print(target_list)

# Output: { 'Directorate', 'Department', 'Unit'}
# Note that the order of the output is not stable
