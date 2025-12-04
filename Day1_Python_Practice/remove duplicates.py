numbers=[2,34,52,95,27,52,34]
uniqueList=[]
for num in numbers:
    if num not in uniqueList:
        uniqueList.append(num)
print(uniqueList)
