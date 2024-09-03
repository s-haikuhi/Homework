# Lesson 21.
"""
9. Dictionaries Exercise:
Write a function that finds the key with the maximum value in a dictionary.
"""
famous_dates = {"Michael Jackson": 1979, "The Beatles": 1964, "System of a Down": 2006, "Andrea Bocelli": 1994,
                "Rammstein": 1999}


def find_max_value_key(my_dict: dict) -> str:
    max_value = 0
    key = ""
    for k, w in my_dict.items():
        if w > max_value:
            max_value = w
            key = k
    return key


print(find_max_value_key(famous_dates))

# Output: System of a Down
