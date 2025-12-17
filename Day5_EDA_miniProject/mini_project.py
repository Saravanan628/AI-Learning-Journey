#Exploratory Data Analysis for Titanic Dataset
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df=sns.load_dataset("titanic")  #loaded dataset
print(df.columns)  #examining columns
pd.set_option('display.max_columns',None)  #setting upto display all values of the columns
print(df.head(10))#finding the target column in the dataset using the values pattern

"""From the above ,we could see the values of some of the columns are numerical datas.And also the data 
in each row represents the data of a passenger"""

print(df.shape)

print(df.isnull().sum()) #Missing value count has been examined

"""The missing count is maximum in the deck column compared to age column"""

#Univariate Analysis
sns.histplot(data=df,x='age')  #For age feature analysis
plt.title("Distribution of Age")
plt.show()
"""From age Distribution, it is found that count is more in the range of age of 20 to 40 """

sns.histplot(data=df,x='fare')
plt.title('Distribution of Fare ')
plt.show()

"""From the fare Distribution, it is found that high fare paid is only in a short value and low fare was used by 
more than 80 percent people"""

#Categorical analysis of univariate
sns.countplot(data=df,x='survived')
plt.title("Survival Distribution")
plt.show()
"""More person were dead compared to alive"""

sns.countplot(data=df,x='class')
plt.title("Class Distribution")
plt.show()
"""From the distribution, it represents more number of people belongs to third class"""

sns.countplot(data=df,x='sex')
plt.title("Gender Distribution")
plt.show()
"""It represents male passengers are more in number"""


#Bivariate / Multivariate Analysis
sns.barplot(data=df,x='sex',y='survived')
plt.title('Gender vs survival')
plt.show()
"""on comparing, it is found that female has survived more compared with male"""

sns.barplot(data=df,x='pclass',y='survived')
plt.title('Passenger class vs Survival')
plt.show()
"""Passengers in class 1 has higher percent of survival compared with other class"""

sns.boxplot(data=df,y='age',x='survived')
plt.title('age vs survival')
plt.show()

sns.violinplot(data=df,y='fare',x='survived')
plt.title('Fare vs Survived')
plt.show()
"""This violin plot shows that passengers who survived generally paid higher fares than those who did not."""

#Correlation between features
corr=df.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
"""from the heatmap, higher fare leads to higher chances of survival.
pclass has a negative correlation with survival.
both fare and class are negatively correlated as the Higher class passengers paid higher fares due to INVERSE ENCODING of pclass"""