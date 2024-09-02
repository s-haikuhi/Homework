# Lesson 12.
"""
Exercise 7: Find the youngest student
Write a function that takes a dictionary with information about students. Return info
about the youngest student
Dictionary example
students_info = {
'student1': {
'name': 'John Doe',
'age': 20,
'subjects': ['Math', 'Physics', 'English'],
'scores': [7, 9, 9, 6],
},
'student2': {
'name': 'Jane Smith',
'age': 19,
'subjects': ['Chemistry', 'Biology', 'History'],
'scores': [5, 6, 8, 10],
},
'student3': {
'name': 'Bob Johnson',
'age': 21,
'subjects': ['Computer Science', 'Statistics', 'Psychology'],
'scores': [8, 8, 9, 9, 9],
},
}
"""


def find_youngest(students_info: dict) -> dict:
    age_youngest = 123
    youngest_info = {}
    for w in students_info.values():
        if w['age'] < age_youngest:
            age_youngest = w['age']
            youngest_info = w
    return youngest_info


print(find_youngest({
    'student1': {
        'name': 'John Doe',
        'age': 20,
        'subjects': ['Math', 'Physics', 'English'],
        'scores': [7, 9, 9, 6],
    },
    'student2': {
        'name': 'Jane Smith',
        'age': 19,
        'subjects': ['Chemistry', 'Biology', 'History'],
        'scores': [5, 6, 8, 10],
    },
    'student3': {
        'name': 'Bob Johnson',
        'age': 21,
        'subjects': ['Computer Science', 'Statistics', 'Psychology'],
        'scores': [8, 8, 9, 9, 9],
    },
}))

# Output: {'name': 'Jane Smith', 'age': 19, 'subjects': ['Chemistry', 'Biology', 'History'], 'scores': [5, 6, 8, 10]}
