
class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def dance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.basketball)
print(harry.dance)




