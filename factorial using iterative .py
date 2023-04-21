def fact(number):
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    return fact
     
n = int(input("Enter the number:-"))
print("factorial of %d is ="%n,fact(n))
