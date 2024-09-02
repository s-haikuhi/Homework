# 7. Lesson
"""
2. Count.
Count all letters, digits and special symbols from a given string.
Sample Input                            Sample Output
P@#yn26at^&i5ve                         Total counts of chars, digits, and symbols
                                        chars = 8
                                        digits = 3
                                        symbol = 4
"""
# 2. SOLUTION

# Case 1.

target = 'P@#yn26at^&i5ve'
CharQuantity = 0
DigitQuantity = 0
SymbolQuantity = 0

for i in target:
    if ord(i) in range(65, 91):
        CharQuantity += 1
    elif ord(i) in range(97, 123):
        CharQuantity += 1
    elif i.isdigit():
        DigitQuantity += 1
    else:
        SymbolQuantity += 1
print(f'Total counts of chars, digits and symbols '
      f'\nchars = {CharQuantity} '
      f'\ndigits = {DigitQuantity} '
      f'\nsymbol = {SymbolQuantity}')

# Output:
"""
Total counts of chars, digits and symbols  
chars = 8
digits = 3
symbol = 4
"""

# Case 2.

target = 'P@#yn26at^&i5ve'
CharQuantity = 0
DigitQuantity = 0
SymbolQuantity = 0

for i in target:
    if 65 <= ord(i) <= 90:
        CharQuantity += 1
    elif 97 <= ord(i) <= 122:
        CharQuantity += 1
    elif i.isdigit():
        DigitQuantity += 1
    else:
        SymbolQuantity += 1
print(f'Total counts of chars, digits and symbols '
      f'\nchars = {CharQuantity} '
      f'\ndigits = {DigitQuantity} '
      f'\nsymbol = {SymbolQuantity}')

# Output:
"""
Total counts of chars, digits and symbols  
chars = 8
digits = 3
symbol = 4
"""

# Case 3.

target = 'P@#yn26at^&i5ve'
CharQuantity = 0
DigitQuantity = 0
SymbolQuantity = 0

for i in target:
    if i.isalpha():
        CharQuantity += 1
    elif i.isdigit():
        DigitQuantity += 1
    else:
        SymbolQuantity += 1
print(f'Total counts of chars, digits and symbols '
      f'\nchars = {CharQuantity} '
      f'\ndigits = {DigitQuantity} '
      f'\nsymbol = {SymbolQuantity}')

# Output:
"""
Total counts of chars, digits and symbols  
chars = 8
digits = 3
symbol = 4
"""
