# ex- 9 9*9=81 and 8+1 = 9
n = int(input("enter a number: "))
a = n*n
x = 0
for i in range(a):
    if a>0:
        p = a%10
        x = x+p
        a = a//10
if n==x:
    print(f"{x} is neon number")
else:
    print(f"{x} is not a neon number")