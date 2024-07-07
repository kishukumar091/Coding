'''
def isprime(x):
    if x<=1:
        return 0
    for i in range(2,int(x/2)):
        if x%i==0:
            return 0
    return 1
n=int(input("Enter Number: "))
if isprime(n):
    print("prime number")
else:
    print("Not a prime number")'''


'''def unique(L):
    unique_list = sorted(list(set(L)))
    return unique_list
list_1 = [4, 2, 1, 3, 2, 4, 5, 1, 6]
print("Unique Elements in Sorted Order:", unique(list_1))
'''

def printPascal(n):
	for i in range(1,n+1):
		for j in range(1,n-i+1):
			print(" ",end=" ")
		C = 1
		for j in range(1,i+1):  
			print(C, end = "   ")
			C = int(C * (i - j) / j)
		print("")
x =int(input("Enter number"))
printPascal(x)

from math import factorial
def print_pascals_triangle(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
        print()
n = 5
print_pascals_triangle(n)