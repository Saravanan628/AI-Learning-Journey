import numpy as np
arr=np.ones((5,5),dtype='int')
arr[0,:]=0
arr[:,0]=0
arr[:,4]=0
arr[4,:]=0
print(arr)