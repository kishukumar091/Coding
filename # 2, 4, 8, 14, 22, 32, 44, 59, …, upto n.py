# 2, 4, 8, 14, 22, 32, 44, 58, …, upto n terms. [Take n as input]
n=int(input("Enter number: "))
x=1
while(x<=n):
    y=x*(x-1) + 2
    x=x+1
    print(y)