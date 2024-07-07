# 1, 2, 5, 10, 17, 26, 37, 50, …, upto n terms. [Take n as input]
n=int(input("Enter number:"))
x=0
while(x<=n):
    y=x**2+1
    x=x+1
    print(y)