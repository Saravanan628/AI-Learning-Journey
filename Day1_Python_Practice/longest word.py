fruits=['apple','banana','orange','pomogranate']
maxlen=len(fruits[0])
word=fruits[0]
for char in fruits:
    if len(char)>maxlen:
        maxlen=len(char)
        word=char
print(word)
