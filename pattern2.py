n = int(input("enter how many rows u need to print:"))
def kk():
    for i in range(n+1):
        for j in range(i):
            print("*",end=" ")
        print("\n")
kk()
"""
*

* *

* * *

* * * *

* * * * *
"""