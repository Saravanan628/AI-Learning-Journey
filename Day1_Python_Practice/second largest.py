numbers=[12,43,27,46,37,94]
firstmax=numbers[0]
secondmax=numbers[0]
for number in numbers:
    if number>firstmax:
        secondmax=firstmax
        firstmax=number
    elif number >secondmax and number != firstmax:
        secondmax=number
print("The second maximum is : ",secondmax)