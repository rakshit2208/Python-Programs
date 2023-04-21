def multiply(*args):
    mul=1
    for i in args:
        mul=mul*i
    return mul
print(multiply(1,2,3,4))