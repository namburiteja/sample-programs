m = int(input("how many times u need to display:"))
n = int(input("enter how many rows you want:"))
k = int(input("enter how many columns you want:"))
def kk():
    for v in range(m):
        for i in range(0,n):
            for j in range(0,k):
                print("*",end=" ")
            print("\n")
kk()

"""
output -->
* * * *
* * * *
* * * *
* * * *
"""