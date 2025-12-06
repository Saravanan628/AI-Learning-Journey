import numpy as np

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
row_sum=np.sum(arr,axis=1)
print("Row_Sum: ",row_sum)
col_sum=np.sum(arr,axis=0)
print("Col_Sum: ",col_sum)
#print("Diagonal: ",arr[0][0],arr[1][1],arr[2][2])
print("Diagonal: ",np.diag(arr))