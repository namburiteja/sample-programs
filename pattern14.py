n = int(input("enter a value: "))
l = ["A","B","C","D","E","F"]
for i in range(1,n+1):
    for j in range(6-i):
        print(l[j],end=" ")
    print()
"""
A B C D E
A B C D
A B C
A B
Ah
"""