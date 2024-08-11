x = input().split()
n = [int(item) for item in x]
'''
l = []
l.append(n[0])
for i in n:
    if i not in l:
        l.append(i)
print(l)   #0 duplicated array
l.sort()
print(l)#sorted array
'''
s = set(n)
ll = list(s)
ll.sort()
print(ll) # sorted array