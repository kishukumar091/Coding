n=int(input("Enter number: "))
fact=1
if n<0: 
    print("not possible")
elif n==0:
    print("factorial is ",fact)
else:
    while(n>=1):
        fact=fact*n
        n=n-1
    print("factorial is",fact)
