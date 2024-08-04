n = int(input("enter value :"))
n = int(n/2)
first_num = 0
second_num = 1
for i in range (0,n):
    print(first_num)
    print(second_num)
    first_num += second_num
    second_num += first_num 