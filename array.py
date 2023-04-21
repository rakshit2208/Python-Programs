from array import*
student = array('i',[])
n = int(input("Enter number of elements:-"))
for i in range(n):
    student.append(int(input("Enter %d elements:-"%i)))
for j in range(len(student)):
    print("Element",j,"is","=",student[j])
  