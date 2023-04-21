class Employee:
   

    def __init__(self, aname, asalary, aage):
        self.name = aname
        self.salary = asalary
        self.age = aage

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.age}"
a = Employee("Harry", 255, 20)
print(a.name,a.salary,a.age)


