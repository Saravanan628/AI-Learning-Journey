number=int(input("Enter the number: "))
def perfect(number):
    sum=0
    for i in range(1,number-1):
        if number%i==0:
            sum+=i
    if sum==number:
        print("Perfect number")
    else:
        print("Not a perfect number")
perfect(number)