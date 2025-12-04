filename = input("Enter file name: ")


with open(filename, "a") as file:
    data = input("Enter text to append to the file: ")
    file.write("\n" + data)

print("Data appended successfully!")
