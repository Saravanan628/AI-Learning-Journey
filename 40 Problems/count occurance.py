word=input("Enter the text: ")
count={}
for char in word:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print("The occurance of each character in the word is: ",count)