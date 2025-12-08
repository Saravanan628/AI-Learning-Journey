import pandas as pd

student={
    "Name":["ajay","akash","bala","dhi","yuvan"],
    "age":[12,13,15,16,13],
    "marks":[67,85,98,87,56]
}
df=pd.DataFrame(student)
df['Pass/Fail']=df['marks']>70
df['Pass/Fail']=df['Pass/Fail'].replace({True:'Pass',False:'Fail'})
print(df)