# Lesson 10: While Loop Exercises
"""
Exercise 2:
Write a Python program that asks the user to enter a password. Keep asking for the
password until the correct password "secret" is entered. Provide appropriate feedback
to the user.
"""
# Case 1.

password = input("Password: ")
target_pas = "secret"

if target_pas == password:
    print("Have successfully logged in.")
else:
    while target_pas != password:
        password = input("Incorrect password (escape using uppercase letters, numbers or other symbols)."
                         " Please try again: ")
        while target_pas == password:
            print("Have successfully logged in.")
            break
# Output: Have successfully logged in.

# Case 2.

password = input("Password: ")
target_pas = "secret"

while password != target_pas:
    if len(password) != len(target_pas):
        password = input(f"Incorrect password: the password length to be of {len(target_pas)} \nPlease try again: ")
    else:
        password = input("Incorrect password (escape using uppercase letters, numbers or other symbols)."
                         " Please try again: ")
if password == target_pas:
    print("Have successfully logged in.")

# Output: Have successfully logged in
