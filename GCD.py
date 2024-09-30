n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))
k = min(n1,n2)
for i in range(1,k+1):
    if(n1%i==0 and n2%i==0):
        l = i
print(l)