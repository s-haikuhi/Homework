# Lesson 21
"""
12. List Exercise:
Write a function that returns the nth largest element from a list.
"""
# Case 1
target_list = [100, 110, 130, 60, 70, 150, 55, 190, 88, 77, 180, 240]
target_list_copy = target_list.copy()
largest_element_index = 4


def nth_largest_in_list(given_list: list, nth: int) -> str:
    max_n = given_list[0]
    list_desc = []

    while len(given_list) > 0:
        max_n = given_list[0]
        for i in given_list:
            if i >= max_n:
                max_n = i
        list_desc.append(max_n)
        given_list.remove(max_n)
    if nth <= len(list_desc):
        nth_largest = list_desc[nth - 1]
    else:
        raise ValueError(f"the number {largest_element_index} is out of range: choose an element within "
                         f"{range(1, len(list_desc) + 1)} : *{len(list_desc) + 1} excluded.")
    return nth_largest


print(nth_largest_in_list(target_list, largest_element_index))

# Output: 150


# Case 2. with .sort() function

def find_nth_largest(g_list: list, nth_largest: int) -> int:
    g_list.sort(reverse=True)
    return g_list[nth_largest - 1]


print(find_nth_largest([100, 110, 130, 60, 70, 150, 55, 190, 88, 77, 180, 240], 4))

# Output: 150
