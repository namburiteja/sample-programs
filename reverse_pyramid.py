n = int(input("enter how many lines: "))
def reverse_pyramid_pattern():
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for k in range(2*n-(2*i+1)):
            print("*",end=" ")
        for l in range(i):
            print(" ",end=" ")
        print("\n")
reverse_pyramid_pattern()
"""
* * * * * * * * *

  * * * * * * *

    * * * * *

      * * *

        *
formula  =  2*n -(2*i+1)
"""