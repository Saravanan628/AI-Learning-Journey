class Operation:
    def __init__(self,data):
        self.data=data


    def __add__(self,other):
        total= self.data+other.data
        return Operation(total)

    def display(self):
        return f"The sum of the two data is {self.data}"

op1=Operation(10)
op2=Operation(20)
op3=op1+op2
print(op3.display())
