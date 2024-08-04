n = input("enter a string: ")
n1 = n[::-1]
if n==n1:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")