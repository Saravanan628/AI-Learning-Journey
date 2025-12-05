class InvalidKeyError(Exception):
    pass

try:
    data={'a':1,'b':2,'c':3,'d':4}
    text=input("Enter the key: ")
    if text not in data:
        raise InvalidKeyError("The given key is not present in data")

except InvalidKeyError as e:
    print("Error: ",e)

else:
    print("Key found in data")
