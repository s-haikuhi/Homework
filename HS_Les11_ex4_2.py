# Lesson 11. Functions & Dictionaries
"""
4.2. Write a python program which concat 2 dicts.
"""


def concat_dicts(dict1: dict, dict2: dict) -> dict:
    for k, w in dict2.items():
        dict1[k] = w
    return dict1


print(concat_dicts({"Country": "France", "City": "Paris"}, {"Company": "New Generation", "Name": "Will"}))


# Output: {'Country': 'France', 'City': 'Paris', 'Company': 'New Generation', 'Name': 'Will'}
