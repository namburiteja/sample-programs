n = int(input("enter a number: "))
k = n
count = 0
while(n>0):
    x = n%10
    count+=1
    n = n//10
print(f"number of digits in {k} are {count}")
"""
enter a number : 56745
number of digits in 56745 are 5
"""