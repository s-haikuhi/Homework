# Lesson 15.
"""
2. Random Password Generator:
Write a function that generates a random password for the user. Allow the user to
specify the length and complexity of the password (include letters, numbers, and
symbols).
hint: (string.ascii_letters, string.digits,string.punctuation)
"""
import random
import string


def generate_password(user_num, letters=False, digits=False, symbols=False):
    generate_pass = ""
    if letters:
        generate_pass += string.ascii_letters
    if digits:
        generate_pass += string.digits
    if symbols:
        generate_pass += string.punctuation

    password = ""

    if letters:
        password += random.choice(string.ascii_letters)
    if digits:
        password += random.choice(string.digits)
    if symbols:
        password += random.choice(string.punctuation)
    i = len(password)
    while i < user_num:
        password += random.choice(generate_pass)
        i += 1
    return password


print(generate_password(int(input(f'Fill in the Number (password length): ')), True, True, True))
