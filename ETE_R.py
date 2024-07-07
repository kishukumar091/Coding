n=int(input("Enter Number: "))
fact=1
if n<0:
    print("Enter Positive Number")
elif n==0 or n==1:
    print(fact)
else:
    while n>=1:
        fact=fact*n
        n=n-1
    print(fact)

string = "ababababab"
substring = "ab"
count = 0
n = 0
while n < len(string):
    x = string.find(substring, n)
    if x == -1:
        break
    count=count + 1
    n = x + 1
print(f"The substring '{substring}' occurs {count} times in the given string.")


str="kishukishukishukishu"
sub="kishu"
cot=0
q=0
while q<len(str):
    h=str.find(sub,q)
    if h==-1:
        break
    cot=cot+1
    q=h+1
print(f"The substring '{sub}'occurs {cot} times in the given string")