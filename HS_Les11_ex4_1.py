# Lesson 11. Functions & Dictionaries
"""
4.1 Write a python function, which add a new value
with given key in dict.
"""


def employee_id(key: str, value: str, dictionary: dict) -> dict:
    dictionary[key] = value
    return dictionary


print(employee_id("Name", "Emili", {"Position": "Senior Accountant",
                                    "Department": "Finance and Accounting"}))

# Output: {'Position': 'Senior Accountant', 'Department': 'Finance and Accounting', 'Name': 'Emili'}
