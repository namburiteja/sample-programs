n = int(input("enter how many lines: "))
def num():
    for i in range(n):
        for j in range(5-i):
            print("*",end=" ")
        print("\n")
num()
"""
* * * * *

* * * *

* * *

* *

*
"""