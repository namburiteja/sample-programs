n = int(input("enter value:"))
s = 1
for i in range(1,n+1):
    if i%2==0:
        s = 0
    else:
        s = 1
    for j in range(i):
        print(s,end=" ")
        s=1-s
    print()

"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""