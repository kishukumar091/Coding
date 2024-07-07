# 1, 2, 4, 7, 11, 16, 22, 29, …, upto n terms. [Take n as input]
n=int(input("Enter input n: "))
x=1
while(x<=n):
    y=x*(x-1)/2+1
    x=x+1
    print(y)
