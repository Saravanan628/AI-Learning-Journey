
try:
    num1 = int(input("Enter the number1: "))
    num2 = int(input("Enter the number2: "))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("Num 2 should not be zero")
except ValueError:
    print("Enter the valid integer")
finally:
    print("Execution completed")