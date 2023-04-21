class Employee:
        no_of_leaves = 10
        def __init__(self, aname):
            self.name = aname
        
        def printdetails(self):
            return f"The Name is {self.name}."

@classmethod
def change_leaves(cls,newleaves):
    cls.no_of_leaves = newleaves

a = Employee("Harry")

a.change_leaves(20)
print(a.no_of_leaves)
