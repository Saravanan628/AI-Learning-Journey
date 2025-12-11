import numpy as np

# Input
X = np.array([[0.5, 1.2, -0.3]])

# Hidden layer weights and bias
W1 = np.array([
    [0.1, -0.2, 0.3, 0.4],
    [0.5, -0.1, 0.2, 0.1],
    [-0.3, 0.4, -0.5, 0.2]
])
b1 = np.array([[0.01, 0.02, -0.01, 0.03]])

# Output layer weights and bias
W2 = np.array([
    [0.2, -0.4],
    [0.1, 0.3],
    [-0.2, 0.1],
    [0.5, -0.3]
])
b2 = np.array([[0.0, 0.1]])

# Forward pass
Z1 = np.dot(X, W1) + b1
A1 = np.maximum(0, Z1)        # ReLU activation
Z2 = np.dot(A1, W2) + b2

# Softmax
exp_vals = np.exp(Z2 - np.max(Z2))
probs = exp_vals / np.sum(exp_vals)

prediction = np.argmax(probs)

print("Hidden layer output:", A1)
print("Output logits:", Z2)
print("Probabilities:", probs)
print("Predicted class:", prediction)

