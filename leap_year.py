n = int(input("enter a year: "))
if (n%100==0 & n%400==0): #divided by 100 means it is century year. A century year which is divided by 400 is a leap year
    print(f"{n} is a leap year")
elif (n%4==0 & n%100!=0): #not divided by a 100 means it is not a century year. A year divided by 4 is a leap year
    print(f"{n} is not a leap year") 