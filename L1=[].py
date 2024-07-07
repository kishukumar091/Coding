L=[]
x=int(input())
for i in range (x):
    L.append(input())
print(L)

#Append
L1=[12,10,45,43]
o='kishu'
L1.append(o)
print("After Append L1=:",L1)

#Extend
L2=[83,18,45,8,10]
L3=[12,34,67]
L2.extend(L3)
print('After Extend L2=',L2)

#Insert
L4=[346,18,45,33]
L4.insert(2,10)
print('After Insert L4 =',L4)

#Delete
L5=[34,'kishu',18,'Dhoni','rohit',10]
del L5[3]
print('After Delete L5 =',L5)

#Clear
L5.clear()
print('After clear L5 =',L5)

#Remove
L6=[10,34,'Dhoni',18,45]
L6.remove('Dhoni')
print('After Remove L6=',L6)

#POP
L7=[76,90,92,'kishu','Vivek','virat','kanhaiya']
elem=L7.pop(3)
print(elem,L7)

#Mutability
A=[1,2,3,4,5,6,8,9,7]
A[0]=2
print(A)

B=[98,87,76,65,54,51]
B[-1]=69
print(B)

C=[6763,783,236,2378]
C[0:4]=[87,27,279,272,778,789,8655,67899]
print(C)

D=[673,237,89,893,6378,908]
D[0:3]=[78,90,0,70,84,70]
print("D",D)

E=[21,31,34,455,67,86]
E[0:0]=[12,39,89,78,90]
print("E",E)

#Function and Method
l1=[1,14,16,18,15]
print(all(element>10 for element in l1))
print(any(element>10 for element in l1))
print(list(enumerate(l1)))
print(len(l1))

l2=[2,4,6,9,0,10,45]
print(max(l2))
print(min(l2))
print(sorted(l2))
print(sum(l2))
print(list(reversed(l2)))

x = ['z', 'f', 'e', 'a','b', 'g', 't'] 
x.sort() 
print(x)
x.sort(reverse = True) 
print(x)
