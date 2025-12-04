amt=int(input("Enter the Amount: "))
rate=int(input("Enter the rate of interest: "))
time=int(input("Enter the time period: "))
def simpleInt(Amount,Rate,Time):
    Int=(Amount*Rate*Time)/100
    print(Int)
simpleInt(amt,rate,time)