'''L=[]
x=int(input("Length of List: "))
for i in range (x):
    L.append(input())
print(L)'''
'''
L1=[9,4,50,'Kishu',91,56]

print(list(reversed(L1)))'''


'''string='This is my Pen'
x=string.upper()
print(x.split())'''

'''L1=[]
n=int(input("Enter Length of List:"))
for i in range(n):
    L1.append(input())
print("L1=",L1)'''
'''x=L1[0:n:2]
print(x)'''



'''L1=[]
n=int(input("Enter Length of List:"))
for i in range(n):
    L1.append(input())
print("L1=",L1)
L2=[]
for i in range(n):
    L2.append(input())
print("L2=",L2)
L3=[]
for i in range(n):
    e=L1.pop(n-n)
    f=L2.pop(n-n)
    L3.append(e+f)
print("L3=",L3)'''

'''#Fibonacci Sequence
x, y = 0, 1
print(x)
while y < 50:
    print(y)
    x, y = y, x + y'''

'''#Write a Python program to demonstrate various ways of 
#accessing the string- By using Indexing and slicing.
my_string = "Hello, World!"
print(my_string[0])
print(my_string[:5])
print(my_string[-6:-1])
print(my_string[::2])'''


'''S ="Weekend"
vowels = "aeiouAEIOU"
x = ""
for char in S:
  if char in vowels:
    x = x + char
  else:
    x =x + "_"
print(x)'''

'''Write a Python program to split to extract a list of the 
words in a sentence. These words are then converted to 
uppercase letters within the list.'''
'''l1=[1,2,34,5,6,778,0]
n=len(l1)

print(l1[:n:2])'''