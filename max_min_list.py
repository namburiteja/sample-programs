n = [4,7,1,4,5,6,6,6,3,21,67]
max = n[0] 
min = n[0]

"""n.sort()
print(f"{n[0]} is smallest number in list")
print(f"{n[-1]} is biggest number in list")"""

for i in n:
    if max < i:
        max = i
    if min > i:
        min = i
print(f"{min} is smallest number in list")
print(f"{max} is biggest number in list")
print(n)