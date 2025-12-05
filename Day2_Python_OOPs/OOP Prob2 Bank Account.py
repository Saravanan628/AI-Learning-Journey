class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            return f"Amount withdrawn Successfully.{self.balance} is the remaining amount"
        elif amount <=0:
            return "Amount should be greater than 0"
        else:
            return "Insufficient Balance"

    def deposit(self,amount):
        if amount<=0:
            return f"Invalid deposit amount"
        self.balance+=amount
        return f"{amount} deposited successfully. Current Balance is {self.balance}"


b1=BankAccount(1000)
print(b1.withdraw(500))
print(b1.deposit(2400))