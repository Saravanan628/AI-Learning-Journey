import pandas as pd

df=pd.read_csv("Employees_Missing.csv")
df['Age']=df['Age'].fillna(df['Age'].median())
df['Age']=df['Age'].astype('int')
print(df)