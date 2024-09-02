# Lesson 12
"""
Exercise 4: Find Index Function
Write a function that finds the index of a given element in a list. If the element is not
present, return -1.
"""
# Case 1.


def find_index(given_element, target_list: list) -> int:
    my_index = 0
    step = 0

    if given_element not in target_list:
        return -1
    else:
        for i in target_list:
            my_index = step
            if i == given_element:
                return my_index
            else:
                step += 1


print(find_index("brave", [1, 2, "kind", "brave", "wise", 4, 5]))


# Output: 3


# Case 2.

def find_index_of_given_element(given_element, given_list: list) -> int:
    if given_element not in given_list:
        return -1
    else:
        return given_list.index(given_element)


print(find_index_of_given_element("lovely", [1, 2, "kind", "brave", "wise", 4, 5]))

# Output: -1
