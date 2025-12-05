import json
import csv


data=[]
with open("people2.csv") as file:
    reader=csv.reader(file)
    for row in reader:
        data.append(row)

with open("people2data.json","w") as f:
    json.dump(data, f, indent=4)

print("file converted to json successfully")