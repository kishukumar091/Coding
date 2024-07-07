ch=input("Enter a character:")
if len(ch)==1:
    if ch=='a'or'e'or'i'or'o'or'u'or'A'or'E'or'I'or'O'or'U':
    #if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        print(ch,"is Vowel")
    else:
        print(ch,"is consonant")
else:
    print("Enter only one character")