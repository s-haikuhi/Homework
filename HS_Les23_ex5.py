# Lesson 23
"""
5. Filtering Word Lengths:
○ Given a list of words, create a dictionary where keys are words, and values are
their lengths, but only for words with lengths greater than 3.
"""

given_list = ["01", "trustworthy", "by", "open-minded", "high_proficiency", "4", "experienced", "with sense of humor"]


def create_dict(g_list: list, filter_point: int) -> dict:
    return {k: len(k) for k in g_list if len(k) > filter_point}


print(create_dict(given_list, 3))
# Output
"""
{'trustworthy': 11, 'open-minded': 11, 'high_proficiency': 16, 'experienced': 11, 'with sense of humor': 19}
"""