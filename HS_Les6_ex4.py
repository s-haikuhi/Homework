# 6. LESSON
"""
Exercise 4: Palindrome Checker
Write a program that prompts the user to enter a word and checks if it is a
palindrome. A palindrome is a word that reads the same backward as forward.
Use string slicing and an if-else statement to compare the original word with its
reverse.
"""
# 4. SOLUTION

palindrome_word = input('Your answer: ')
n = -1
palindrome_check = palindrome_word[:int(len(palindrome_word)/2)]
palindrome = False

for i in palindrome_check:
    if i == palindrome_word[n]:
        palindrome = True
        n -= 1

if palindrome is True:
    print(f'{palindrome_word} is a palindrome!')
else:
    print(f'{palindrome_word} is NOT a palindrome!')

# Output for the user inputs ['civic','mom', 'level', 'anna', '22-02.20-22', "Ararat', 'bella'] accordingly:
"""
civic is a palindrome!
mom is a palindrome!
level is a palindrome!
anna is a palindrome!
22-02.20-22 is a palindrome!
Ararat is NOT a palindrome!
bella is NOT a palindrome!
"""

