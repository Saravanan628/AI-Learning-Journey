dict1={"a":1,"b":2,"c":3}
dict2={"d":4,"e":5,"f":6}
mergedDict={}
for key in dict1:
    mergedDict[key]=dict1[key]
for key in dict2:
    mergedDict[key]=dict2[key]
print(mergedDict)