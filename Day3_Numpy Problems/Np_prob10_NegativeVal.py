import numpy as np

np.random.seed(10)
arr=np.random.randint(-100,100,size=10)
pos=arr[arr>0]
print("Original Array: ",arr)
print("The positive elements are: ",pos)