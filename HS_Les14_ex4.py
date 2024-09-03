# Lesson 14.
"""
File Splitting:
Develop a Python Function that reads a large text file (input.txt) and splits it
into smaller files, each containing a specified number of lines. Function parameter the number of lines
per file. Generate multiple output files (output1.txt, output2.txt, etc.).
"""


def file_splitting(file_to_split, lines_number):
    with open(file_to_split, "r") as file:
        content = file.read()
        new_content = content.split("\n")
        n = 0
        num = 1
        i = 1
        n_files = 0
        filename = "file_" + str(num) + ".txt"
        if len(new_content) % lines_number != 0:
            n_files = len(new_content) // lines_number + 1
        while i <= n_files:
            with open(filename, "w") as nf:
                nf.write("\n".join(new_content[n:n + lines_number]))
                n += lines_number
                i += 1
                num += 1
                filename = "file_" + str(num) + ".txt"


print(file_splitting("Listening_Test.txt", 6))
