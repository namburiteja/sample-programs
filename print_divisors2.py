import math
n = int(input("enter a number: "))
l = []
k = int(math.sqrt(n))
for i in range(1,k+1):
    if n%i==0:
        l.append(i)
        if n/i!=i:
            l.append(int(n/i))
l.sort()
print(l)