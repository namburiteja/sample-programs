n = int(input("enter value: "))
l = ["A","B","C","D","E","F"]
for i in range(1,n+1):
    for j in range(n-i):
        print("k",end=" ")
    for k in range(i):
        print(l[k],end=" ")
    for m in range(i-1):
        print(l[m],end=" ")
    print()