import pandas as pd
df=pd.read_csv("Employees_Missing.csv")
df['Name']=df['Name'].str.strip()
print(df)
