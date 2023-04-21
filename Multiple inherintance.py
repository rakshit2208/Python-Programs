class Employee:

    def __init__(self, name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}"


class Player:
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game =game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class Programer(Player,Employee):
    pass

Janak=Employee("janak",5000,"instructor")
Mohan=Player("Mohan",["cricket,chess,football"])
Rajesh=Programer("Rajesh","Cricket")
print(Rajesh.printdetails())

