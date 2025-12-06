import numpy as np

np.random.seed(10)
arr=np.random.randint(1,100,size=20)
greater=arr[arr>50]
print("Array Generated: ",arr)
print("Greater Elements: ",greater)