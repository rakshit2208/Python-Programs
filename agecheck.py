print("What is your age:-",end='')
age = int(input())
if age<18:
    print("You can not drive.")
elif age==18:
    print("We will think about you.")
else:
    print("You can drive.")
