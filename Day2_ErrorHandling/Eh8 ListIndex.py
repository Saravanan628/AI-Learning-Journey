class ListIndexError(Exception):
    pass

try:
    data=[1,23,43,65,32]
    ind=int(input("Enter the index value: "))
    if ind<0 or ind>=len(data):
        raise ListIndexError("Given Index Out of range")

except ListIndexError as e:
    print("Error: ",e)

except ValueError:
    print("Enter a valid integer")

else:
    print(f"Valid Index and value is {data[ind]}")

finally:
    print("Program executed")