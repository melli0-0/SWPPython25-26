from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

class Company:

    def __init__(self, name: str):
        self.name = name
        self.departments = []

    def total_employees(self):
        return sum(len(d.employees) for d in self.departments)

    def total_departments(self):
        return len(self.departments)

    def gender_ratio(self):
        m = f = 0
        for d in self.departments:
            for e in d.employees:
                if e.gender == Gender.MALE:
                    m += 1
                elif e.gender == Gender.FEMALE:
                    f += 1

        total = m + f
        if total == 0:
            return {"male": 0, "female": 0}
        return {"male": (m / total) * 100, "female": (f / total) * 100}


class Department:

    def __init__(self, name: str):
        self.name = name
        self.employees = []
        self.head = None

    def total_employees(self):
        return len(self.employees)


class Person:

    def __init__(self, name: str, gender: Gender):
        self.name = name
        self.gender = gender


class Employee(Person):

    def __init__(self, name: str, gender: Gender, department: Department):
        super().__init__(name, gender)
        self.department = department


class DepartmentHead(Employee):

    def __init__(self, name: str, gender: Gender, department: Department):
        super().__init__(name, gender, department)