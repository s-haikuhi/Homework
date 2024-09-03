# Lesson 14
"""
3. File Concatenation:
Write a Python script that takes multiple text files as input and concatenates their
contents into a single text file.
"""


def concatenate_my_files(file1, file2):
    with open(file1, "r") as f1:
        content1 = f1.read()
    with open(file2, "r") as f2:
        content2 = f2.read()
    with open("combined_file.txt", "w") as new_file:
        new_file.write(f'{content1} \n {content2}')
    with open("combined_file.txt", "r") as nf:
        return nf.read()


print(concatenate_my_files("experimenting.txt", "output1.txt"))
