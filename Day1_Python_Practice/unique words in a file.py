filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read()

words = text.split()
unique_words = set(words)

print("Unique words in the file:")
for word in unique_words:
    print(word)
