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

    def add_department(self, dep):
        self.departments.append(dep)



class Department:

    def __init__(self, name: str):
        self.name = name
        self.employees = []
        self.head = None

    def total_employees(self):
        return len(self.employees)

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_head(self, dep_head):
        self.head = dep_head


class Person:

    def __init__(self, name: str, gender: Gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return self.name


class Employee(Person):

    def __init__(self, name: str, gender: Gender, department: Department):
        super().__init__(name, gender)
        self.department = department
        self.department.add_employee(self)

    def __str__(self):
        return super().__str__()


class DepartmentHead(Employee):

    def __init__(self, name: str, gender: Gender, department: Department):
        super().__init__(name, gender, department)

    def __str__(self):
        return super().__str__()


if __name__ == '__main__':

    mellis_comp = Company("Mellis Company")

    finance = Department("Finance")
    software = Department("Software")

    mellis_comp.add_department(finance)
    mellis_comp.add_department(software)

    silvana = Employee("Silvana", Gender.FEMALE, department=software)
    melli = Employee("Melli", Gender.FEMALE, department=software)
    kili = Employee("Kili", Gender.MALE, department=finance)

    finance.add_head(kili)
    software.add_head(silvana)

    print(f"Gender ratio: {mellis_comp.gender_ratio()}")
    print(f"Total departments: {mellis_comp.total_departments()}")
    print(f"Total employees: {mellis_comp.total_employees()}")
    print(f"Employees in {software.name}: {software.total_employees()}")
    print(f"Head of {finance.name}: {finance.head}")