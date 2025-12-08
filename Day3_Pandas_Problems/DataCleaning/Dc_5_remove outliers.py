import pandas as pd
df=pd.read_csv("Employees_Missing.csv")
Q1=df['Salary'].quantile(0.25)
Q3=df['Salary'].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
df = df[(df['Salary'] >= lower) & (df['Salary'] <= upper)]
print(df)