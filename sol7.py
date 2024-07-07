n = int(input("Enter a number: "))
d = {x:x*x for x in range(1,n+1)}
print("d =",d)

'''dix = {'apple': 5, 'banana': 2, 'orange': 4, 'kiwi': 3}
ascending = dict(sorted(dix.items(), key= lambda item: item[1]))
descending = dict(sorted(dix.items(), key=lambda item: item[1], reverse=True))
smallest_value = min(dix.values())
largest_value = max(dix.values())
print(ascending)
print(descending)
print(smallest_value )
print(largest_value) '''


'''with open('input.txt', 'r') as file:
    content = file.read()
with open('output.txt', 'w') as file:
    file.write(content)
print("File read and write operation completed successfully!")'''

