n = int(input("enter value: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(n-i):
        print(" ",end=" ")
    for l in range(n-i):
        print(" ",end=" ")
    for m in range(1,i+1):
        print(j,end=" ")
        j = j-1
    print()
"""
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1
"""