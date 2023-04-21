#map functon
number = ["1","5","4","8","10"]
number = list(map(int,number))
number = number[4]+1
print(number)
# square program
num1 = [1,2,3,4,5,6,7]
num1 = list(map(lambda x:x*x,num1))
print(num1)
#filter functon
list1 = [1,2,3,4,5,6,7,8,9]
def greater(num):
    return num>5
num2 = list(filter(greater,list1))
print(num2)
