from array import*
a=array('i',[])
n=int(input("Enter number of element in array:-"))
for i in range(n):
    a.append(int(input("Enter %d elements:-"%i)))
for i in range(len(a)):
    print("element",i,"is","=",a[i])

print("Array after insert:-")
a.insert(2,49)
a.insert(3,80)
n = len(a)
i=0 
while i<n:
    print(a[i])
    i=i+1
