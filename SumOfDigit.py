num=int(input("Enter number:"))
sum=0
while(num!=0):
    r=num%10
    num=num//10
    sum=sum+r
print(sum)