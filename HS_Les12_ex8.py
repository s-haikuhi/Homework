# Lesson 12.
"""
Exercise 8: Find student with the highest average score
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
}
"""


def highest_average_score(students_info: dict) -> dict:
    highest_score_average = 0
    highest_score_info = {}
    for w in students_info.values():
        sum_score = 0
        for i in w["scores"]:
            sum_score += i
        average_helper = sum_score / len(w['scores'])
        if average_helper > highest_score_average:
            highest_score_average = average_helper
            highest_score_info = w
    return highest_score_info


print(highest_average_score({
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
    }
}))

# Output: {'name': 'Bob Johnson', 'age': 21, 'subjects': ['Computer Science', 'Statistics', 'Psychology'],
# 'scores': [8, 8, 9, 9, 9]}
