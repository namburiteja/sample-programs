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
patternpyramid()
"""
        *

      * * *

    * * * * *

  * * * * * * *

* * * * * * * * *

formula =  2*i+1
"""