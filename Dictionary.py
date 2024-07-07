month={1:'jan',2:'feb',3:'march',4:'april',5:'may',6:'june'}
'''print(month)
print(type(month))
print(month[4])
print(month.get('dec'))

#for key in month
for i in month:
    print(month[i],end=' ')
print()

#for value in month
for j in month:
    print(j,end=' ')
print()'''
'''for key, value in month.items():
    print(f"{key}: {value}")'''

'''for i,j in month.items():
    #print(key,value,end=' ') 
    print(i,':',j,',',end=' ')
'''

print(len(month))



'''
#Delete in dictionary
print(month.pop(4))

print(month.popitem())
print(month)

del month[5]
print(month)

print(month.clear())


#Add something in dictionary
month[8]='august'
print(month)'''


month[3]='kishu'
print(month)