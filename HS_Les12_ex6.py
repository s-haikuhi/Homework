# Lesson 12.
"""
Exercise 6: Count Words Function
Write a function that counts the number of words in a sentence.
"""


# Case 1. Optimal Solution

def count_words_in_expression(given_expression: str) -> int:
    return len(given_expression.split())


print(count_words_in_expression(" Ich spreche kein Französisch. "))

# Output: 4


# Case 2. Longest way

def count_words(given_expression: str) -> int:
    total_count_words = 1
    helper = " "
    j = 0

    if given_expression.strip() == "":
        return 0
    elif helper not in given_expression.strip():
        return total_count_words
    else:
        while j < len(given_expression):
            for i in given_expression.strip():
                if i != helper:
                    j += 1
                    continue
                else:
                    total_count_words += 1
                    j += 1
                    continue
            return total_count_words


print(count_words(" Ich spreche kein Französisch. "))

# Output: 4
