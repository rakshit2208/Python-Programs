class Employee:
   

    def __init__(self, aname, asalary, aage):
        self.name = aname
        self.salary = asalary
        self.age = aage

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.age}"

    @classmethod
    def from_dash(cls,string):
        #p=string.split("-")
        #print(p)
        #return cls(p[0],p[1],p[2])
        return cls(*string.split("-"))



a = Employee("Harry", 255, 20)
b = Employee.from_dash("Mohan-40-200")
print(b.name)
print(a.name)


