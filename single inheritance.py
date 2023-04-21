class Employee:

    def __init__(self, name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}"


class Programmer(Employee):
    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages


    def prog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and Role is {self.role}.The languages are {self.languages}"

Ram = Employee("Ram", 2555, "Instructor")
Rohan = Employee("Rohan", 4557, "Student")

shubham = Programmer("Shubham", 5553, "Programmer", ["python","c"])
karan = Programmer("Karan", 7772, "Programmer",["C++","Java"])
print(shubham.prog())
print(karan.prog())
print(Ram.printdetails())
