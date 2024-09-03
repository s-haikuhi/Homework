# Lesson 23
"""
3. Vowels in a Word:
○ Create a list of vowels present in a given word.
"""


def create_list_vowels(given_expression: str) -> list:
    vowels = ["a", "e", "i", "o", "u", "y"]
    return list(set([i for i in given_expression if i in vowels]))


print(create_list_vowels("modern architecture"))
# Output presented for non_duplicate values of vowels
"""
['u', 'i', 'e', 'a', 'o']
"""