n = int(input("enter how many lines: "))
def patternpyramid():
    for i in  range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
        for k in range(2*i+1):
            print("*",end=" ")
        for l in range(n-i-1):
            print(" ",end=" ")
        print("\n")
def reverse_pyramid_pattern():
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for k in range(2*n-(2*i+1)):
            print("*",end=" ")
        for l in range(i):
            print(" ",end=" ")
        print("\n")
patternpyramid()
reverse_pyramid_pattern()
"""
        *

      * * *

    * * * * *

  * * * * * * *

* * * * * * * * *

* * * * * * * * *

  * * * * * * *

    * * * * *

      * * *

        *
"""