# Lesson 21
"""
6. Tuple Exercise:
Create a tuple of student names and their corresponding scores. Write a function to find
the student with the highest score.
"""
students = ["Areg", "Arpy", "Narek", "Natali", "Eduard", "Emili"]
scores = [95, 65, 114, 80, 77, 100]


def max_score_student(students_list, scores_list):
    my_dic = {}
    students_with_scores = []
    for i, j in zip(students_list, scores_list):
        my_dic[i] = j
        students_with_scores.append(my_dic)
    students_tuple = tuple(students_with_scores)

    max_score = scores[0]
    student_with_high_score = {}

    for j in students_tuple:
        for k, v in j.items():
            if v > max_score:
                student_with_high_score = {}
                max_score = v
                student_with_high_score[k] = v
    return student_with_high_score


print(max_score_student(students, scores))

# Output: {'Narek': 114}
