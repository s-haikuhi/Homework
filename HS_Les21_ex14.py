# Lesson 21
"""
14. Strings Exercise:
Write a function that capitalizes the first letter of each word in a sentence.
"""
target_sentence = """I have always thirsted for knowledge,
I have always been full of questions."""


def capitalize_words_in_sentence(sentence):
    helper = sentence.split()
    step = 0
    for i in helper:
        helper[step] = i.capitalize()
        step += 1
    my_sentence = " ".join(helper)
    return my_sentence


print(capitalize_words_in_sentence(target_sentence))

# Output
"""
I Have Always Thirsted For Knowledge, I Have Always Been Full Of Questions.
"""
