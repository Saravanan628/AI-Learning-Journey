text=input("Enter the text: ")
char=input("Enter the char: ")
count=0
for ch in text:
    if ch==char:
        count+=1

print("The count of occurance of ",char,"is: ",count)