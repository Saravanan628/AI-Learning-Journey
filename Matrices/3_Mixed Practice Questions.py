import numpy as np

a=np.array([[1,2],[2,1]])
b=np.array([[3,4],[5,6]])
print("Sum: ",a+b) #Addition of matrices
k=5
print("Scalar Multi: ",k*a) #Scalar Multiplication
print("Matrix mult :",np.matmul(a,b)) #Matrix mult
print("Norm: ",np.linalg.norm(b))  #Frobenius norm

A = np.array([[1,2,3], [4,5,6]])
B = np.array([[1,2], [3,4], [5,6]])
print(a@b)


