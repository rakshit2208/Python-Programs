number=int(input("Enter any number you want to check this number is prime or not:-"))
count = 0
for i in range(1,number+1):
    if number%i==0:
        count=count+1
if count==2:
    print("%d is prime number."%number)
else:
    print("%d is not a prime number."%number)