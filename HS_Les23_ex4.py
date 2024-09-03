# Lesson 23
"""
4. Character ASCII Values:
○ Given a string, create a dictionary where keys are characters, and values are
their ASCII values.
"""
given_string = ("Unconditional*trustworthy!8.#BRAVEHEART,6:@"
                " %& Work-life balance;")

target_dict = lambda my_text: {k: ord(k) for k in my_text}
print(target_dict(given_string))

# Output
"""
{'U': 85, 'n': 110, 'c': 99, 'o': 111, 'd': 100, 'i': 105, 't': 116, 'a': 97, 'l': 108, '*': 42, 'r': 114, 
'u': 117, 's': 115, 'w': 119, 'h': 104, 'y': 121, '!': 33, '8': 56, '.': 46, '#': 35, 'B': 66, 'R': 82, 'A': 65, 
'V': 86, 'E': 69, 'H': 72, 'T': 84, ',': 44, '6': 54, ':': 58, '@': 64, ' ': 32, '%': 37, '&': 38, 'W': 87, 
'k': 107, '-': 45, 'f': 102, 'e': 101, 'b': 98, ';': 59}
"""