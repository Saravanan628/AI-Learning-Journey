import numpy as np

x=np.array([1.0,-2.0])

w1=np.array([[0.4,-0.3,0.1],
             [0.2,0.5,-0.4]])

b1=np.array([0.1, -0.2,0.05])
z1=np.dot(x,w1)+b1
print("Z1: ",z1)

W2 =np.array( [
    [0.3, -0.1],
    [-0.2, 0.4],
    [0.6, -0.3]
])
b2 =np.array([0.0, 0.2])

A1=1/(1+np.exp(-z1))
print("Activation function: ",A1)
z2=np.dot(A1,W2)+b2
print("Output logits: ",z2)

exp_vals = np.exp(z2 - np.max(z2))
probs = exp_vals / np.sum(exp_vals)
print("Probabilities: ",probs)

prediction = np.argmax(probs)
print("Predictions: ",prediction)
