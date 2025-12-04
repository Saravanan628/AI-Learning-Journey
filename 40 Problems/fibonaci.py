number=int(input("Enter the number: "))
def fibo(num):
    num1=0
    num2=1
    for i in range(num):
        print(num1)
        num3=num1+num2
        num1=num2
        num2=num3
fibo(number)