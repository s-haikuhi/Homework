# Lesson 13.
"""
2. Write a Python program to find if a given string starts with a given
character using Lambda.
"""
# Case 1.

same_start = lambda ch, given_expression: ch == given_expression[0]

print(same_start("h", "sunny days are ahead"))
# Output: False

print(same_start("s", "sunny days are ahead"))
# Output: True


# Case 2.

check_if_start_the_same = lambda char_to_check, expression: expression.startswith(char_to_check)

print(check_if_start_the_same("S", "Strong communication skills"))
# Output: True
