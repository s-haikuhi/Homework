# 6. LESSON
"""
Exercise 2: Vowel Counter
Write a program that takes a string as input and counts the number of vowels (a,
e, i, o, u) in the string. Use a for loop, an if statement, and the in operator to
check if a character is a vowel.
"""
# 2. SOLUTION

# Case 1.

course = input("Course name: ")
vowels_list = ['a', 'e', 'i', 'o', 'u']
quantity_vowels = 0

for a in course:
    if a.lower() in vowels_list:
        quantity_vowels += 1
print(quantity_vowels)

# Output: 7 for the input 'Auf Wiedersehen!'
