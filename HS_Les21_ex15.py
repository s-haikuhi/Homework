# Lesson 21
"""
15. Multiple Exceptions:
Write a function that performs the following tasks:
Accepts a list and an index as input.
Attempts to access the element at the given index in the list.
Handles both IndexError
Uses a finally block to print "Task completed" regardless of whether an exception
occurred or not.
"""


def access_to_list_element(given_list: list, list_index: int):
    return given_list[list_index]


try:
    print(access_to_list_element(["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag",
                            "Samstag", "Sonntag"], 7))
except IndexError as e:
    print(f"The mentioned index is out of range. Index Error is occurred: \n{e}")
finally:
    print("Task is completed.")

# Output
"""
The mentioned index is out of range. Index Error is occurred: 
list index out of range
Task is completed.
"""
