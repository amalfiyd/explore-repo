import numpy as np
import h5py
import pandas as pd
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

# Helper
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def loss(ytrain, yhat, epsilon=1e-5):
    c1 = ytrain * np.log(yhat + epsilon)
    c2 = ((1 - ytrain) * np.log(1 - yhat + epsilon))
    return (c1, c2, -1/m * np.sum(c1 + c2))

    # return (0, 0, 1/m * np.sum(np.power(yhat-ytrain, 2)))

def forward_propagation(X, W, b):
    z = np.dot(W, X) + b
    return sigmoid(z)

def back_propagation(X, y, yhat):
    m = X.shape[1]
    dz = yhat - y
    dw = np.dot(dz, X.T) / m

    db = np.sum(dz) / m

    return dw, db

# Preparing dataset
# -- breast cancer dataset
# dataset = load_breast_cancer()
# m = dataset.data.shape[0]
# nFeat = dataset.data.shape[1]
#
# Xtrain = dataset.data.reshape(nFeat, m)
# Xtrain_norm = (Xtrain - np.min(Xtrain)) / (np.max(Xtrain) - np.min(Xtrain))
# ytrain = dataset.target.reshape(1, m)

# -- wisconsin breast cancer dataset
# filename = r'D:\OneDrive\Projects\03 - Explore\00 - Deeplearning.ai\00 Logistic Regression\winsconsin.csv'
# df = pd.read_csv(filename)
# ytrain = np.array(df.diagnosis)
# ytrain = np.where(ytrain == "M", 1, 0)
#
# list = ['Unnamed: 32','id','diagnosis']
# Xtrain = np.array(df.drop(list, axis=1)).T
# Xtrain_norm = (Xtrain - np.min(Xtrain)) / (np.max(Xtrain) - np.min(Xtrain))
#
# m = Xtrain.shape[1]
# nFeat = Xtrain.shape[0]

# -- cat or no cat dataset
filename = r'D:\OneDrive\Projects\03 - Explore\00 - Deeplearning.ai\00 Logistic Regression\train_catvnoncat.h5'
f = h5py.File(filename, 'r+')
Xtrain = np.array(f['train_set_x'][:])
Xtrain = Xtrain.reshape(Xtrain.shape[0], -1).T
Xtrain_norm = Xtrain / 255.

m = Xtrain_norm.shape[1]
nFeat = Xtrain_norm.shape[0]

ytrain = np.array(f['train_set_y'][:])
ytrain = ytrain.reshape(1, m)

# Hyper Parameters
numIter = 10000
alpha = 0.003

# Parameters random setup
W = np.random.rand(1, nFeat)
b = np.random.rand(1, 1)

# Tracking parameters
losses = []
xaxis = []
X = Xtrain_norm
for i in range(numIter):
    print("Running iteration " + str(i))

    # Forward Propagation
    yhat = forward_propagation(X, W, b)

    # Loss function calculation
    c1, c2, closs = loss(ytrain, yhat)
    losses.append(closs)
    xaxis.append(i)

    # Back Propagation
    dw, db = back_propagation(X, ytrain, yhat)

    # Update parameters
    W = W - (alpha * dw)
    b = b - (alpha * db)

    # break

# Plotting cost function
plt.plot(xaxis, losses)
plt.show()

