class AgeExceptionError(Exception):
    pass
try:
    age=int(input("Enter the age: "))
    if age<18:
        raise AgeExceptionError("Age should be greater than 18")

except AgeExceptionError as e:
    print("Error: ",e)
