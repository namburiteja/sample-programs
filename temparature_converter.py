temp = int(input("enter the temparature: "))
ckff = input("enter c or k or f: ")
ckf = ckff.lower()
c = 0
k = 0
f = 0
if ckf=='c':
    f = temp*(9/5)+32
    k = float(temp+273.15)
    print(f"if temperature is {temp} celsius then")
    print(f"fahrenheit temparature is {f} and")
    print(f"kelvin temparature is {k}")
elif ckf == 'k':
    c = temp - 273.15 
    f = (temp-273.15)*1.8+32
    print(f"if temperature is {temp} kelvin then")
    print(f"fahrenheit temparature is {f} and")
    print(f"celsius temparature is {c}")
elif ckf == 'f':
    c = (temp-32)*5/9
    k = (temp-32)*5/9+273.15
    print(f"if temperature is {temp} fahrenheit then")
    print(f"kelvin temparature is {k} and")
    print(f"celsius temparature is {c}")
else:
    print("enter correct string")