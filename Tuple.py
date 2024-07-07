my_list=[]
x=int(input("Length of List: "))
for i in range (x):
    my_list.append(input())
print(my_list)
my_tuple=tuple(my_list)
print(my_tuple)

print(('ac')*2)
print(('ac',)*2)
print((1, 2, 3) > (1, 0, 3)  )
print(tuple({1:10, 2:20}) )

origtup = (1, 5, 3, 4, 7, 9, 1, 27) 
sorttup = sorted(origtup) 
print(sorttup) # Result: [1, 1, 3, 4, 5, 7, 9, 27] 
print(origtup) # Result: (1, 5, 3, 4, 7, 9, 1, 27)
print(tuple(sorttup))#Result:(1, 1, 3, 4, 5, 7, 9, 27)
print(sum(origtup))
print(min(("P", "y", "t", "h", "o", "n", "k"))) 
print(tuple("hello")) 