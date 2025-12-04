text=input("Enter the text: ")

def palindrome(text):
    i = 0
    j = len(text)
    while(i<j):
       if text[i]!=text[j-1]:
          return False
       i+=1
       j-=1
    return True
result=palindrome(text)
print(result)

#using slicing
if(text==text[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")
