#sum of all elements in array
from array import*
a = array('i',[])
num = int(input("Enter number of elements:-"))
for i in range(num):
    a.append(int(input("Enter %d elements:-"%i)))
    
for i in range(len(a)):
    print("Elements",i,"is","=",a[i])
sum = 0
for i in range(len(a)):
    sum = sum + a[i]
print("Sum of all elements are=",sum)