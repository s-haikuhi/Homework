# Lesson 11. Functions & Dictionaries
"""
4.3. Write a python function, which create a dictionary
for given number N, where keys are numbers from
1 to N, and values are cubs of that numbers
"""


# Case 1.

def dict_given_number(number: int) -> dict:
    i = 1
    new_dict = {}
    while i <= number:
        new_dict[i] = i ** 3
        i += 1
    return new_dict


print(dict_given_number(10))


# Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}


# Case 2.

def create_dict_given_num_as_key(given_number: int) -> dict:
    target_dict = {}
    for n in range(1, given_number + 1):
        target_dict[n] = n ** 3
    return target_dict


print(create_dict_given_num_as_key(10))

# Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
