# Lesson 21
"""
2. Class Exercise:
Create a Python class representing a basic calculator with methods for addition,
subtraction, multiplication, and division.
"""
from statistics import mean


class Workforce:
    current_workforce_num = None

    def __init__(self, company_name, workforce_number, hired, resigned, hiring_target_rate):
        self.name = company_name
        self.workforce_num = workforce_number
        self.num_new_hired = hired
        self.num_resigned = resigned
        self.hiring_targets = hiring_target_rate

    def workforce_after_hiring(self):  # addition
        self.current_workforce_num = self.workforce_num + self.num_new_hired
        return self.current_workforce_num

    def workforce_after_resignation(self):  # subtraction
        self.current_workforce_num -= self.num_resigned
        return self.current_workforce_num

    def hiring_target(self):  # multiplication
        return self.num_new_hired * self.hiring_targets

    def turnover_rate(self):  # division
        return self.num_resigned / mean([self.workforce_num, self.current_workforce_num])


company1_workforce = Workforce("X-way", 2000, 450, 200, 0.2)
print(company1_workforce.workforce_after_hiring())
print(company1_workforce.workforce_after_resignation())
print(company1_workforce.hiring_target())
print(company1_workforce.turnover_rate())
