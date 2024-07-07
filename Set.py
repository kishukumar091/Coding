student_id = {112, 114, 116, 118, 115} 
print('Student ID:', student_id)

 
vowel_letters = {'a', 'e', 'i', 'o', 'u'} 
print('Vowel Letters:', vowel_letters) 


mixed_set = {'Hello', 101, -2, 'Bye'} 
print('Set of mixed data types:', mixed_set)

#Create an enpty set
Empty_set=set()
print('Data Type of Empty_set:',type(Empty_set))

#dublicate Item in set
number={10,23,45,45,46}
print("number=",number)

print('DataType=',type(number))

print("length=",len(number))

for x in number:
    print(x,end=' ')
print()
print(67 in number)

number.remove(10) 
print('number=',number)

number.discard(46)
print('number=',number)

number.add(3)
print('number=',number)

number.update([23,48,566])
print('number=',number)

print(number.pop())
print('number=',number)

print(number.pop())
print('number=',number)

number.clear()
print('number=',number)

