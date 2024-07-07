'''n=int(input("Enter number: "))
while n>=0:
    print(n)
    n=n-1'''

'''n=int(input("Enter number: "))
rev=0
while n!=0:
    r=n%10
    n=n//10
    rev=rev*10+r
print(rev)'''

n=int(input("Enter number:"))
r=0
sum=0
for i in range(n):
    r=r*10+2
    sum=sum+r
print(sum)