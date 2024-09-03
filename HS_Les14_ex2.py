# Lesson 14
"""
Find and Replace:
Implement a Python program that reads a text file (input.txt), prompts the user
for a word to find, and another word to replace it with. Replace all occurrences of
the first word with the second word and save the modified text to a new file
(output.txt).
"""


def replace_word(find_word, replace_with, my_file):
    with open(my_file, "r") as f:
        content = f.read()
    changed_content = ""
    if find_word in content:
        changed_content += content.replace(find_word, replace_with)
    with open("output2.txt", "w") as new_file:
        new_file.write(changed_content)
    with open("output2.txt", "r") as my_new_file:
        return my_new_file.read()


print(replace_word(input(f'a word to find: '), input(f'a word to replace: '), "experimenting.txt"))
