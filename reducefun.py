from functools import reduce
list1 = [1,2,3,4,5]
num = reduce(lambda x,y:x+y,list1)
print(num)
num = reduce(lambda x,y:x-y,list1)
print(num)
num = reduce(lambda x,y:x*y,list1)
print(num)

