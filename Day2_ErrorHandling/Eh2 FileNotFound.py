file=None
try:
    file=open("employees_list.txt","r")

except FileNotFoundError:
    print("File is not available ")

finally:
    if file is not None:
        file.close()
