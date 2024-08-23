n = int(input("enter how many lines: "))
def numbers():
    for i in range(n+1):
        for j in range(i):
            print(i,end=" ")
        print("\n")
numbers()
"""
1

2 2

3 3 3

4 4 4 4

5 5 5 5 5
"""