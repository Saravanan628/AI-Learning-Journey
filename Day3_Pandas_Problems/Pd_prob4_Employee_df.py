import pandas as pd

employee={
    "Name":["ram","varun","saran","paari"],
    "Dept":["sales","testing","software","analyst"],
    "salary":[45654,76543,123433,54566]
}
df=pd.DataFrame(employee)
print("Employee Data: \n",df)