# Lesson 21
"""
4. List Exercise:
Write a function that takes two lists and returns a new list containing only the common
elements. (without using set)
"""
# Case 1.

commons_list = list(filter(lambda n: n in [1, 2, 3, 4, "eins", "zwei", "drei"], [2, 4, 6, 8, "eins", "zwei", "drei"]))
print(commons_list)

# Output: [2, 4, 'eins', 'zwei', 'drei']


# Case 2.

def list_of_commons(list1: list, list2: list):
    my_new_list = []
    for i in list1:
        if i in list2:
            my_new_list.append(i)
    return my_new_list


print(list_of_commons(["five", "seven", 1, 4, 6, 8], ["five", "ten", 4, 6, 10]))

# Output: ['five', 4, 6]
