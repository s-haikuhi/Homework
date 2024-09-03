# Lesson 13.
"""
13. Sets Exercise:
Write a function that checks if two sets are disjoint (have no common elements).
"""
jan_bonuses = {10, 20, 30, 40, 50, 60}
feb_bonuses = {45, 50, 55, 60, 65, 70, 80, 90, 100}


def check_if_disjoint(set1, set2):
    if len(set1 & set2) == 0:
        return True
    else:
        return False


print(check_if_disjoint(jan_bonuses, feb_bonuses))

# Output: False
