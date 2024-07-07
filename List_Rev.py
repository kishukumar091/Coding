a='kishu singh123!!!'
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Kishu","Singh"))
print(a.capitalize())
print(a.count('k'))
print(a.title())
print(a.find("g"))
print(a.center(10))
print(a.swapcase())


main_string = "ababababab"
substring = "ab"

count = 0
start_index = 0

while start_index < len(main_string):
    index = main_string.find(substring, start_index)

    if index == -1:
        break

    count += 1
    start_index = index + 1

print(f"The substring '{substring}' occurs {count} times in the given string.")
