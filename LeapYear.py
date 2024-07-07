n=int(input("number: "))
if(n%100==0 and n%400==0):
    print(n," is a leap Year")
elif(n%4==0 and n%100!=0):
    print(n," is a leap Year")
else:
    print(n," is not a leap Year")
