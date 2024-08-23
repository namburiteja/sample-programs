n =int(input("enter how many lines u want: "))
def kk():
    for i in range(n+1):
        for j in range(n-i):
            print(j+1,end=" ")
        print("\n")
kk()
"""
1 2 3 4 5

1 2 3 4

1 2 3

1 2

1
"""