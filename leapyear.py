print("Enter any year:-",end="")
n = int(input())
if n%4==0:
    if n%100==0:
        if n%400==0:
            print("%d is a leap year."%n)
        else:
            print("%d is not a leap year."%n)
    else:
        print("%d is a leap year."%n)
else:
    print("%d is not a leap year."%n)
