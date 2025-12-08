import pandas as pd

df=pd.read_csv("Employees_Missing.csv")
df['City']=df['City'].str.strip().str.upper()
df['City']=df['City'].fillna("UNKNOWN")
print(df)