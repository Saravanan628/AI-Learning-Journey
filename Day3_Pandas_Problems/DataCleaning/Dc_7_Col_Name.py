import pandas as pd
df=pd.read_csv("Employee.csv")
df['Tax Amount']=df['Salary']*0.1
df=df.rename(columns={"Tax Amount":"TaxAmount"})
print(df)