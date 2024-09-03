# ClassWork
"""
Write an abstract class with name Employee
Write 2 employee classes by inheriting from abstract Employee
Write function
get_info -> return string with name and position
calculate_salary -> return float with information about employee salary
Calculate salary should be different for 2 classes
"""
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return self.name, self.position

    @abstractmethod
    def calculate_salary(self):
        pass


class IT(Employee):
    def __init__(self, name, position, salary, kpi_bonus):
        super().__init__(name, position, salary)
        self.kpi_bonus = kpi_bonus

    def calculate_salary(self):
        return self.salary * (1 + self.kpi_bonus / 100)


class PR(Employee):
    def __init__(self, name, position, salary, rate, project_reward):
        super().__init__(name, position, salary)
        self.rate = rate
        self.project_reward = project_reward

    def calculate_salary(self):
        if 10 <= self.rate:
            return self.salary + self.project_reward * self.rate / 100


employee1 = IT("Areg", "Senior Software Engineer", 1500000, 45)
employee2 = PR("Natali", "Senior PR Specialist", 500000, 11, 100000)

print(employee1.get_info())
print(employee1.calculate_salary())

print(employee2.get_info())
print(employee2.calculate_salary())

# 2. Classwork
"""
Write an abstract class with name GeometricFigure
Write 2 geometric figure classes by inheriting from GeometricFigure
Write 2 functions
get_perimeter -> return perimeter of figure
get_area -> return area of figure
"""

from math import sqrt


class GeometricFigure(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    def get_area(self):
        pass


class Rectangle(GeometricFigure):
    def __init__(self, length, height, name):
        self.length = length
        self.height = height
        self.name = name

    def get_perimeter(self):
        return self.name, round(2 * (self.length + self.height),2)

    def get_area(self):
        return self.name, round(self.length * self.height, 2)


class RectangularTriangle(GeometricFigure):
    def __init__(self, leg1, leg2, name):
        self.height = leg1
        self.base = leg2
        self.name = name

    def get_perimeter(self):
        return self.name, self.height + self.base + round(sqrt(self.height ** 2 + self.base ** 2), 2)

    def get_area(self):
        return self.name, round((self.height * self.base) / 2, 2)


GeometricF1 = Rectangle(10, 15, "Rectangle")
GeometricF2 = RectangularTriangle(10, 15, "Rectangular Triangle")


print(GeometricF1.get_perimeter())
print(GeometricF1.get_area())

print(GeometricF2.get_perimeter())
print(GeometricF2.get_area())
