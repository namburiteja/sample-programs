n = int(input("enter how many lines: "))
def numbers():
    for i in range(n+1):
        for j in range(i):
            print(i,end=" ")
        print("\n")
numbers()