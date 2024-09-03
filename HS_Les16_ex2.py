# Lesson 16
"""
2. List Element Removal
Write a function that removes an element at a specified index from a list. Handle the
IndexError by raising a custom exception if the index is out of range.
"""

# Case 1.

given_index = 6
given_list = [1, 2, 3, 4, 5, 6, 7]
remove_an_element = lambda index, target_list: set(target_list) - {target_list[index]}

if given_index >= len(given_list):
    raise IndexError("The index is out of range.")
else:
    given_list = list(remove_an_element(given_index, given_list))
print(given_list)

# Output: [1, 2, 3, 4, 5, 6]


# Case 2.

to_remove_element = lambda my_index, my_list: set(my_list) - {my_list[my_index]}

try:
    print(list(to_remove_element(2, [0, 1, 2, 3, 4, 5, 6])))
except IndexError as e:
    print(e)
finally:
    print("Successfully tested.")

# Output:
"""
[0, 1, 3, 4, 5, 6]
Successfully tested.
"""


# Case 3. Remove with del

def remove_element(ind: int, t_list: list) -> list:
    if ind >= len(t_list):
        raise IndexError("The index is out of the range.")
    else:
        del t_list[ind]
        return t_list


print(list(remove_element(2, ["aufregend", "wunderbar", "gefährlich", "ordentlich"])))

# Output: ['aufregend', 'wunderbar', 'ordentlich']


# Case 4.

def remove_element(given_index: int, given_list: list):
    del given_list[given_index]


try:
    print(remove_element(6, ["a", "b", 3, 4, "c", "d"]))
except IndexError as e:
    print(f'The specified Index is out of range: {e}')

# Output:
# The specified Index is out of range: list assignment index out of range
