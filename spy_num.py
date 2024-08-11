# if we press 123 here 1+2+3=6 and 1*2*3=6 so it is spy number
n = int(input("enter a number: "))
a = n
mul = 1
add = 0
#while a>0:
#    c = a%10
#    add = add + c
#    mul = mul * c
#    a = a//10
for i in range(a):
    if a>0:
        c = a%10
        add = add + c
        mul = mul * c
        a = a//10

if add==mul:
    print(f"{n} is spy number")
else:
    print(f"{n} is not a spy number")