n = int(input("enter value:"))
for i in range(1,n*2):
    s = i
    if i>n:
        s= 2*n-i
    for j in range(s):
        print("*",end=" ")
    print()
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""