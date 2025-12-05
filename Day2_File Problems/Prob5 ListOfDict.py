import json
data=[{"name": "Arun","age":14},
       {"name": "Bala","age":22},
       {"name": "kavi","age":14}]

with open("students.json","w") as file:
     json.dump(data,file,indent=4)

print("Data written into json file")