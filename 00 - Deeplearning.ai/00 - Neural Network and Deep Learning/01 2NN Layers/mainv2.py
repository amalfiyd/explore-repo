import numpy as np
import h5py
import pandas as pd
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

# Helper
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoidp(x):
    return sigmoid(x) * (1 - sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanhp(x):
    return 1 - np.power(tanh(x), 2)

def relu(x):
    return np.maximum(0, x)

def relup(x):
    return np.where(x > 0, 1.0, 0.0)

def lrelu(x):
    return np.maximum(0.01*x, x)

def lrelup(x):
    return np.where(x > 0, 1.0, 0.01)

# Preparing dataset
# -- cat or no cat dataset
# filename = r'D:\OneDrive\Projects\03 - Explore\00 - Deeplearning.ai\00 Logistic Regression\train_catvnoncat.h5'
# f = h5py.File(filename, 'r+')
# Xtrain = np.array(f['train_set_x'][:])
# Xtrain = Xtrain.reshape(Xtrain.shape[0], -1).T
# Xtrain_norm = Xtrain / 255.
#
# m = Xtrain_norm.shape[1]
# nFeat = Xtrain_norm.shape[0]
#
# ytrain = np.array(f['train_set_y'][:])
# ytrain = ytrain.reshape(1, m)

# -- wisconsin breast cancer dataset
filename = r'D:\OneDrive\Projects\03 - Explore\00 - Deeplearning.ai\00 - Neural Network and Deep Learning\00 Logistic Regression\winsconsin.csv'
df = pd.read_csv(filename)
ytrain = np.array(df.diagnosis)
ytrain = np.where(ytrain == "M", 1, 0)

list = ['Unnamed: 32','id','diagnosis']
Xtrain = np.array(df.drop(list, axis=1)).T
Xtrain_norm = (Xtrain - np.min(Xtrain)) / (np.max(Xtrain) - np.min(Xtrain))

m = Xtrain.shape[1]
nFeat = Xtrain.shape[0]

# Hyper Parameters
numIter = 10000
alpha = 3e-5

# Parameters random setup
W1 = np.random.rand(100, nFeat)
W2 = np.random.rand(10, 100)
W3 = np.random.rand(1, 10)
b1 = np.random.rand(100, 1)
b2 = np.random.rand(10, 1)
b3 = np.random.rand(1, 1)

# Tracking parameters
losses = []
xaxis = []
X = Xtrain_norm
epsilon = 1e-5

# Training iteration
for i in range(numIter):
    print("Running iteration : " + str(i))
    # Forward propagation
    z1 = np.dot(W1, X) + b1
    a1 = tanh(z1)

    z2 = np.dot(W2, a1) + b2
    a2 = tanh(z2)

    z3 = np.dot(W3, a2) + b3
    a3 = sigmoid(z3)

    # Loss calculation
    c1 = ytrain * np.log(a3 + epsilon)
    c2 = ((1 - ytrain) * np.log(1 - a3 + epsilon))
    closs = np.average(c1 + c2) * -1

    losses.append(closs)
    xaxis.append(i)

    # Backward propagation
    dz3 = a3 - ytrain.reshape(1, m)
    dw3 = np.dot(dz3, a2.T)
    db3 = np.sum(dz3, axis=1, keepdims=True) / m

    dz2 = np.multiply(np.dot(W3.T, dz3), tanhp(z2))
    dw2 = np.dot(dz2, a1.T)
    db2 = np.sum(dz2, axis=1, keepdims=True) / m

    dz1 = np.multiply(np.dot(W2.T, dz2), tanhp(z1))
    dw1 = np.dot(dz1, X.T)
    db1 = np.sum(dz1, axis=1, keepdims=True) / m

    # Update parameters
    W1 = W1 - (alpha * dw1)
    W2 = W2 - (alpha * dw2)
    W3 = W3 - (alpha * dw3)
    db1 = b1 - (alpha * db1)
    db2 = b2 - (alpha * db2)
    db3 = b3 - (alpha * db3)

    # break

# Plot the losses
plt.plot(xaxis, losses)
plt.show()
