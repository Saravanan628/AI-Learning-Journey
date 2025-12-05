import csv

data=[["name","number"],["arun",12344],["Bala",8765432]]
with open("people2.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)

with open("people2.csv","r") as file:
    reader=csv.reader(file)
    count=0
    for row in reader:
        count+=1
    print(count)


