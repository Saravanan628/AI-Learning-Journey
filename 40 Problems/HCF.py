first=int(input("Enter the first number: "))
second=int(input("Enter the second number: "))
def high(first,second):
    while second!=0:
        temp=first%second
        first=second
        second=temp
    return first
print(high(first,second))

