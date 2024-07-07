tup = (1, 2, 3, 4, 5)
'''
if 3 in tup:
    print("3 is present in the tuple")
else:
    print("3 is not present in the tuple")
a=tup[0]
print("The first item in the tuple is:", a)
print("The last item in the tuple is:", tup[-1])

tup += (6, 7, 8)
print("The updated tuple is:", tup)

print("The length of the tuple is:", len(tup))'''


'''
my_tuple = (1, 2, 3, 4, 5, 1, 2, 3)
repeated_items = []
for item in my_tuple:
    if my_tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)
print("The repeated items in the tuple are:", repeated_items)'''
    

'''set={1,23,34,52,64,6}
print(1 in set)
for item in set:
    print(item,end=' ')
print()
set.add(10)
print(set)'''

'''s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
common_letters = set(s1) & set(s2)
print(set(s1))
print(set(s2))
print('The common letters are:',','.join(common_letters))
print('The common letters are:',','.join(sorted(common_letters)))'''