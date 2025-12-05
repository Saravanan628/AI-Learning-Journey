class Calculator:
    def __init__(self):
        self.num1=int(input("Enter num1: "))
        self.num2=int(input("Enter num2: "))
        self.op=input("Enter the operation: ")

    def calculate(self):
        if self.op=='+':
            total=self.num1+self.num2
            return total
        elif self.op=='-':
            return self.num1-self.num2
        elif self.op=='*':
            return self.num1*self.num2
        elif self.op=='//':
            return self.num1//self.num2
        else:
            return f"Invalid Operation"

c1=Calculator()
print("Result: ",c1.calculate())
