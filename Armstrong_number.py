n=int(input("enter a number: "))
sum=0
b=len(str(n))
x=n
while(n!=0):
    r=n%10
    n=n//10
    sum=sum+r**b
if x==sum:
        print(x,"armstrong")
else:
    print(x,"not armstrong")