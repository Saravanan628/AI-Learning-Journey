import pandas as pd

student={
    "Name":["ajay","akash","bala","dhi","yuvan"],
    "age":[12,13,15,16,13],
    "marks":[67,85,98,87,56]
}
df=pd.DataFrame(student)
print(df[df['marks']>80])