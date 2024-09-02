# Lesson 11. Functions & Dictionaries
"""
4.4 Write a python function which create dict from 2
lists with the same length
"""


# Case 1.

def dict_from_lists(list1: list, list2: list) -> dict:
    target_dict = {}
    n = 0
    if len(list1) == len(list2):
        for i in list1:
            target_dict[i] = list2[n]
            n += 1
        return target_dict


print(dict_from_lists([1, 2, 3, 4], ['Pyhton', 'SQL', 'PowerBI', 'Statistics']))


# Output: {1: 'Pyhton', 2: 'SQL', 3: 'PowerBI', 4: 'Statistics'}


# Case 2.

def create_dict_from_given_lists(g_list1: list, g_list2: list) -> dict:
    target_dict = {}
    for k, v in zip(g_list1, g_list2):
        target_dict[k] = v
    return target_dict


print(create_dict_from_given_lists([1, 2, 3, 4], ['Pyhton', 'SQL', 'PowerBI', 'Statistics']))

# Output: {1: 'Pyhton', 2: 'SQL', 3: 'PowerBI', 4: 'Statistics'}
