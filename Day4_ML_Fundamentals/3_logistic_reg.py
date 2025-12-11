import numpy as np
x=np.array([2.0, -1.0])
w=np.array([0.7, -1.2])
b=0.5
z=np.dot(x,w)+b
prob=1/(1+np.exp(-z))
print("Probability: ",prob)
out=1 if prob>=0.5 else 0
print("output: ",out)