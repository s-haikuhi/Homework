# Lesson 16.
"""
4. Login System
Write a simple login system where the user enters a username and password. Handle
the KeyError by raising a custom exception if the username is not found in the users
database(dictionary).
"""
users_database = {"areg.sun": "a1bc", "narek26": "_fahre", "hayk.s": "142536A", "tigran.great": "str6"}
logIn = input(f'Login: ')


# 4. Solution

if logIn in users_database.keys():
    password = input(f'Password: ')
    if password == users_database[logIn]:
        print("Successfully logged in.")
    else:
        raise ValueError("Incorrect Password")
else:
    raise KeyError('Incorrect Username')

# Output: KeyError: 'Incorrect Username' for the input(Aregak)
