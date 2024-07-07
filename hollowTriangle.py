n=int(input("Enter Number: "))
for i in range(n):
    for j in range(i+1):
        if(j==i or j==0 or i==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
