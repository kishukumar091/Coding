'''n=int(input("Enter nth term: "))
a=int(input("Enter First term: "))
r=int(input("Enter Common Ratio: "))
S=(a*(r**(n)-1))/(r-1)
print("Sum of the series is:",S)'''



def kishu(n):
    ones=n%10
    tens=(n//10)%10
    hundreds=(n//100)%10
    thousands=(n//1000)%10
    return ones,tens,hundreds,thousands

number=int(input("Enter the number: "))
ones,tens,hundreds,thousands=kishu(number)
print(ones,"ones")
print(tens,"tens")
print(hundreds,"hundreds")
print(thousands,"thoudands")