for i in range(1,6):
    for j in range(6,i+1,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("%d"%j,end=" ")
    for j in range(j-2,0,-1):
        print("%d"%j,end=" ")
    print()