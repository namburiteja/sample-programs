n = int(input("enter a number: "))
k = n
sum = 0
while(n>0):
    x = n%10
    sum = sum + (x*x*x)
    n = n//10
if sum == k:
    print(f"{k} is armstrong number")
else:
    print(f"{k} is not armstrong number")