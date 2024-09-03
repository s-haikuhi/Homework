# Lesson 16.
"""
3. URL Validator
3.1 Write a function that validates a URL string. Handle the ValueError by raising a custom
exception if the URL format is invalid.
3.2 Write a function that removes an element at a
specified index from a list. Handle the IndexError by raising a custom exception if the
index is out of range.
"""
# 3.1 Case 1.
import re
import string
protocol = "https://"
protocol1 = "http://"
identifier_part = "."
identifier = "/"
delimiters = r"//|\."


def validate_URL(my_url: str):
    valid = True
    count = 0
    if re.search(f"^{protocol}", my_url) or re.search(f"^{protocol1}", my_url):
        valid = True
        for i in my_url[my_url.find(identifier) + 2:]:
            if i == identifier_part:
                count += 1
        if count >= 1:
            results = re.split(delimiters, my_url)
            if results[-1] == "":
                valid = False
            for j in results[-1]:
                if j not in string.ascii_letters:
                    valid = False
            for k in results[1:]:
                if identifier in k:
                    valid = False
        else:
            valid = False

    else:
        valid = False
    if not valid:
        return f'The URL {my_url} is not valid'
    else:
        return f'The URL {my_url} is valid'


print(validate_URL("https:wwww.3schools.com"))

# Output: The URL https:wwww3schools.com is not valid
