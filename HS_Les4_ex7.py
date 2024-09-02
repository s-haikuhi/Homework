# 4. LESSON: ARITHMETIC OPERATIONS
"""
7.Birth Year:
The program prompts the user their birth year. Assuming a person’s age
is a non-negative integer not exceeding 120, output the user’s age or the
words “Incorrect Year”. The sample outputs assume it’s currently the year
2016. If you are writing this program during any other year, the correct
answers may differ. Store the value of the current year in a variable.
Sample Input            Sample Output
2016                    0
2018                    Incorrect Year
1903                    113
1803                    Incorrect Year
1991                    25
"""
# 7. Solution

birth_year = int(input('Your Birth year = '))
given_year = 2016
age = given_year - birth_year

if 0 <= age <= 120:
    print(age)
else:
    print('Incorrect Birth Year')

# Outputs for the user inputs [2016, 2018, 1903, 1803, 1991] accordingly:
"""
0
Incorrect Birth Year
113
Incorrect Birth Year
25
"""
