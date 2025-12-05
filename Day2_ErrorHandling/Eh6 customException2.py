class InvalidAmountError(Exception):
    pass

try:
    amt=int(input("Enter the amount value: "))
    if amt<0:
        raise InvalidAmountError("Amount should be greater than zero")

except ValueError:
    print("Enter a valid number!")

except InvalidAmountError as e:
    print("Error: ",e)