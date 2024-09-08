n = int(input("enter value: "))
l = ["null","A","B","C","D","E"]
for i in range(1,n+1):
    for j in range(1,i+1):
        print(l[i],end=" ")
    print()
"""
A
B B
C C C
D D D D
E E E E E
"""