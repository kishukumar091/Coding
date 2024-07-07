a=int(input("Enter marks1: "))
b=int(input("Enter marks2: "))
c=int(input("Enter marks3: "))
avg1=(a+b)/2
avg2=(b+c)/2
avg3=(c+a)/2
if(avg1>avg2 and avg1>avg3):
    print("Best test average marks has Marks1 and Marks2:",avg1)
elif(avg2>avg1 and avg2>avg3):
    print("Best test average marks has Marks2 and Marks3:",avg2)
else:
    print("best test average marks has Marks3 and Marks1:",avg3)