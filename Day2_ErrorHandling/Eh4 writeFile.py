file=None
try:
    text=input("Enter the text: ")
    with open("notes.txt","w") as file:
        file.write(text)
except FileNotFoundError:
    print("File is not available")

finally:
    if file is not None:
        file.close()