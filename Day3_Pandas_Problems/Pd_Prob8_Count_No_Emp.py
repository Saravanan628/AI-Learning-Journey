import pandas as pd

employee={
    "Name":["ram","varun","saran","paari","Indhu"],
    "Dept":["sales","testing","software","analyst","sales"],
    "salary":[45654,76543,123433,54566,43213]
}
df=pd.DataFrame(employee)
number=df.groupby('Dept')['Name'].count()
print(number)

df.to_csv('emp.csv')
print('File Converted')
