import pandas as pd
df=pd.read_csv("Employees_Missing.csv")
df['Dept']=df['Dept'].str.strip().str.title()
df['Dept']=df['Dept'].replace({'I.T':'IT','Information Tech':'IT','It':'IT'})
print(df)