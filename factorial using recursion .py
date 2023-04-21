def fact(number):
    if number==1:
        return 1
    else:
        return number*fact(number-1)
     
n = int(input("Enter the number:-"))
print("factorial of %d is ="%n,fact(n))
