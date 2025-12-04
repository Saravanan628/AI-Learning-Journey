number=int(input("Enter the number: "))
def armstrong(number):
    temp=number
    temp1=number
    sum=0
    count=0
    while (temp1 > 0):
        digit = temp1 % 10
        count+=1
        temp1 //= 10
    while(temp>0):
        digit=temp%10
        sum+=digit**count
        temp//=10
    if number==sum:
        print("Armstrong number")
    else:
        print("Not a Armstrong number")
armstrong(number)