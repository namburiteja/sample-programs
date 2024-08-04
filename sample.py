a = int(input());
if(a>0 and a<10):
    print("single digited number");
elif(a>=10 and a<100):
    print("double digited number");
elif(a>=100 and a<1000):
    print("triple digited number");
else:
    print("please enter number below 1000");