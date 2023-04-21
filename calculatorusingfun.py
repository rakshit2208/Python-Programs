print("Enter 1st number:-",end='')
x = int(input())
print("Enter 2nd number:-",end='')
y = int(input())

def add(x,y):
    z = x+y
    print("Additon is :-",z)
add(x,y)

def sub(a,b):
    z = a-b
    print("Subtracton is :-",z)
sub(x,y)

def mul(x,y):
    z = x*y
    print("Multiplication is :-",z)
mul(x,y)

def div(x,y):
    z = x/y
    print("Divition is :-",z)
div(x,y)

def mod(x,y):
    z = x%y
    print("Modulus is :-",z)
mod(x,y)
