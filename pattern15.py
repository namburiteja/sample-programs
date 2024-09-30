n = int(input("enter value: "))
for i in range(1,n+1):
    p = 65
    l = ((2*i-1)/2)
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        if(k<=l):
            p+=1
            print(chr(p-1),end=" ")
        else:
            p-=1
            print(chr(p-1),end=' ')
    for l in range(n-i):
        print(" ",end=" ")
    print()
    """
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
    """