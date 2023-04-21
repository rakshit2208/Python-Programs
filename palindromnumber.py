a = int(input("Enter a number you want to check palindrome or not:-"))
c = a
s = 0
while a>0:
    b = a%10
    s = (s*10)+b
    a = a//10
if s==c:
    print("The number %d is a palindrome."%(c))

else:
    print("The number %d is not a palindrome."%(c))
