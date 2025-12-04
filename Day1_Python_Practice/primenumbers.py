st=int(input("Enter the starting number: "))
ed=int(input("Enter the end number: "))
def prime(start,end):
    for i in range(start,end):
        is_prime=True
        if i<=1:
            is_prime=False
        for j in range(2,i):
            if(i%j==0):
                is_prime=False
                break
        if(is_prime):
            print(i)

prime(st,ed)

