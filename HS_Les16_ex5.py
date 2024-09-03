# Lesson 16.
"""
5. Type Conversion:
Write a function that prompts the user to enter a number and tries to convert it to an
integer. Handle the TypeError exception by printing a message indicating that the input
is not a valid number. Use a finally block to print "Type conversion process completed."
"""
convert_int = lambda user_input: int(user_input)

try:
    convert_int(input(f"Fill in a number: "))
except TypeError as e:
    print(f'Your input is not a valid number: {e}')
finally:
    print("Type conversion process completed.")

# Output:
# ValueError: invalid literal for int() with base 10: 'df'
