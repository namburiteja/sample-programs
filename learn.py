n = int(input("enter a number:"))
i = 1
k = 0
#calculate sum of n natural numbers by using for loop
#for i in range(1,n+1):
#    k = k + i
#print(k)
#calculate sum of n natural numbers by using while loop
while i<=n:
    k+=i
    i+=1
print(k)