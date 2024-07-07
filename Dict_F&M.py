'''dict={1:'kishu',2:'singh',3:'Happy',4:'kishuuu',5:"kisu"}
print(all(dict)) # True
print(len(dict)) # Result:5
print(sorted(dict))

dict2 = {1:'alpha', 2:'', '':'gamma', 4:'music'} 
print(any(dict2)) # Result: True
print(all(dict2)) # Result: False'''

# Clear in dictionary
'''empty={'Name':'kishu','age':20,'exp':5}
print(len(empty)) # return 3
empty.clear() 
print(len(empty)) # Return 0
print(empty.clear()) # Return None'''

# Copy in dictionary
'''kishu = {'apple':'red', 'orange':'orange', 'mango':'yellow'} 
dist=kishu.copy()
print(dist)'''

# Formkeys 
'''Seq = ('one', 'two', 'three') 
dic = dict.fromkeys(Seq,10) 
print(dic) # Result: {'three': 10, 'two': 10, 'one': 10}'''

Dict={'cyan':1, 'violet':2, 'green':3}
print('value:%s'%Dict.get('cyan')) # Return value:1
print('value:%s'%Dict.get('red')) # Return value:None
print(Dict.items()) #dict_items([('cyan', 1), ('violet', 2), ('green', 3)])
print(Dict.keys()) #dict_keys(['cyan', 'violet', 'green'])
print(Dict.values()) #dict_values([1, 2, 3])
Dict.setdefault('yellow',4)
print(Dict) #{'cyan': 1, 'violet': 2, 'green': 3, 'yellow': 4}