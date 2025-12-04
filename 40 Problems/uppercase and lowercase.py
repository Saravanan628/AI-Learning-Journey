text=input("Enter the text: ")
upper=""
lower=""
for char in text:
    if 'a'<=char<='z':
        upper+=chr(ord(char)-32)
    else:
        upper+=char
for char in text:
    if 'A'<=char<='Z':
        lower+=chr(ord(char)+32)
    else:lower+=char
print("UpperCase: ",upper)
print("LowerCase: ",lower)