a=int(input("Kishu:"))
b=int(input("Happy:"))
c=int(input("lucky:"))
if(a>b and a>c):
    print("Kishu is greatest:",a)
elif(b>a and b>c):
    print("Happy is greatest:",b)
else:
    print("lucky is greatest:",c)