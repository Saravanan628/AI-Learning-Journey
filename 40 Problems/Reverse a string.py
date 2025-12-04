text=input("Enter the word: ")

#using reversed
reversed_text1=""
reversed_text1=reversed_text1.join(reversed(text))
print(reversed_text1)

#using loop
reversed_text2=""
for char in text:
    reversed_text2=char+reversed_text2
print(reversed_text2)