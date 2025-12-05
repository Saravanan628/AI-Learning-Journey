import json

with open("people2data.json", "r") as file:
    data=json.load(file)

name=input("Enter name: ")
number=int(input("Enter the number: "))

new_contact={"name":name,"number":number}
data.append(new_contact)

with open("people2data.json","w") as f:
    json.dump(data,f,indent=4)

