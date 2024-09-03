# Lesson 14.
"""
1. Character Count:
Write a Python script that reads a text file (input.txt) and counts the
occurrences of each character (including spaces and punctuation). Output the
character frequency to another text file (output.txt).
"""


# 1. Solution

def count_frequency(expression: str) -> int:
    total_count = 0
    for i in expression:
        total_count += 1
    return total_count


def output_frequency_in_new_file(new_file):
    with open(new_file, "r") as my_file:
        content = my_file.read()
    with open("Output1.txt", "w") as n_file:
        n_file.write(str(count_frequency(content)))
    with open("Output1.txt", "r") as f:
        return f.read()


print(output_frequency_in_new_file("experimenting.txt"))

# Output: 179