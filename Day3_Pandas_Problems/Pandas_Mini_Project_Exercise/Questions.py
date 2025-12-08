import pandas as pd

df=pd.read_csv("Employee.csv")
#print(df)
#print(df.head(5)) #First 5 rows
#print(df.tail(3)) #Last 3 rows
#print(df.shape) #gives Number of rows and columns
#print(df.columns) #Gives column names
#print(df.info()) #gives dataset information
#print(df.describe()) #gives statistical summary(i.e mean,count,sum, median....)

#print(df[df['Salary']>70000]) #gives salary greater than 70000

#print(df[df['City']=='Chennai']) #Person coming from chennai
#print(df[(df['Gender']=='F') & (df['Dept']=='IT')]) #females work in IT department
#print(df[df['Experience']>5]) #Experience greater than 5 years
#print(df[(df['Age']>28) &(df['Age']<33)])  #Age between 28 and 33
#print(df.sort_values(by='Salary',ascending=False)) #sort by salary in descending order
#print(df.sort_values(by='Age', ascending=True)) #sort by age in ascending order
#print(df.sort_values(by=['Dept','Salary'],ascending=[True,False])) #sort by dept,salary in ascend and descend
#print(df.groupby('Dept')['Name'].count())
#print((df.groupby('Dept')['Salary'].mean()))  #Average Salary per department
#print(df.groupby('City')['Experience'].max()) #Maximum experience in each city
#print(df.groupby('Dept')['Salary'].sum())#Total sum paid per department
#print(df.groupby(['Dept','Gender'])['Name'].count())#Number of male vs female per department
#df['SalaryInLakhs']=df['Salary']/100000  #Salary in lakhs
#print(df)
#df['Seniority']=df['Experience'].apply(lambda x:"Junior" if x<3 else("Mid" if x<=7 else "Senior")) #add seniority with following the conditions
#print(df)
#df['Tax Amount']=df['Salary']*0.1  #Calculate tax amount
#print(df)

df2=pd.read_csv("Employees_Missing.csv")
#df2['Salary'].fillna(df2['Salary'].median(),inplace=True) #fill missing values with median salary value
#print(df2)
#df2.dropna(subset=['Experience'],inplace=True) #drop rows with missing values in experience
#print(df2)
#df2.drop_duplicates(inplace=True) #Removes repeated rows
#print(df2)
#print(df2.isnull().sum()) #Missing values in each col

#df2['City']=df2['City'].str.upper() #convert city names to uppercase
#print(df2)
#df2['Dept']=df2['Dept'].str[0:3] #print first three letters in department
#print(df2)

#print(df2[df2['Name'].str[0]=='D']) #Person name start with D

#it_emp=df2[df2['Dept']=='IT']
#it_emp.to_csv("It_Employees.csv")
#print("File saved")

sal_greater=df2[df2['Salary']>60000]
sal_greater.to_csv("Greater_Salary.csv")
print("csv creation success")