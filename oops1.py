class Employee:
    def printdetails(self):
        return (f"Name is {self.name}.Age is {self.age}.Salary is {self.salary}.")
vedant=Employee()
Harshit=Employee()
vedant.name=input("Enter your name:-")
vedant.age=int(input("Enter your age:-"))
vedant.salary=int(input("Enter your salary:-"))
print(vedant.printdetails())
Harshit.name=input("Enter your name:-")
Harshit.age=int(input("Enter your age:-"))
Harshit.salary=int(input("Enter your salary:-"))
print(Harshit.printdetails())
