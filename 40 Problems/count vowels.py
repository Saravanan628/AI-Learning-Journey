text=input("Enter the text: ")
count=0
for char in text:
    if char in "AEIOUaeiou":
        count+=1
print(count)
