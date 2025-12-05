data=input("Enter the number: ")
try:
    num=int(data)
    print("The entered data is: ",num)
except ValueError:
    print("Please enter valid input number")
finally:
    print("Program executed successfully")