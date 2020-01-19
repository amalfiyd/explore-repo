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

list = ['Unnamed: 32', 'id', 'diagnosis']
Xtrain = np.array(df.drop(list, axis=1)).T
Xtrain_norm = (Xtrain - np.min(Xtrain)) / (np.max(Xtrain) - np.min(Xtrain))
X = Xtrain_norm
epsilon = 1e-3

m = Xtrain.shape[1]
nFeat = Xtrain.shape[0]

# Hyper Parameters
numIter = 10000
alpha = 3e-3

# Parameters setup
layers = [20, 10, 1]
numLayers = len(layers)
hiddenLayerActivation = "relu"
outputLayerActivation = "sigmoid"
Ws = [[] for x in range(numLayers)]
bs = [[] for x in range(numLayers)]

for ix in range(numLayers):
    if ix == 0:
        Ws[ix] = np.random.randn(layers[ix], nFeat) * 0.0001
    else:
        Ws[ix] = np.random.randn(layers[ix], layers[ix-1]) * 0.0001
    bs[ix] = np.zeros((layers[ix], 1))

# Tracking parameters
losses = []
xaxis = []

_zs = [[] for x in range(numLayers)]
_as = [[] for x in range(numLayers)]
_dzs = [[] for x in range(numLayers)]
_dws = [[] for x in range(numLayers)]
_dbs = [[] for x in range(numLayers)]

for i in range(numIter):
    print("Running iteration : " + str(i))

    # Forward propagation
    for ix in range(numLayers):
        if ix == 0:
            z = np.dot(Ws[ix], X) + bs[ix]
            a = relu(z)
            _zs[ix] = z
            _as[ix] = a
        elif ix == numLayers-1:
            z = np.dot(Ws[ix], _as[ix - 1]) + bs[ix]
            a = sigmoid(z)
            _zs[ix] = z
            _as[ix] = a
        else:
            z = np.dot(Ws[ix], _as[ix - 1]) + bs[ix]
            a = relu(z)
            _zs[ix] = z
            _as[ix] = a

    # Loss function
    c1 = ytrain * np.log(_as[numLayers-1] + epsilon)
    c2 = ((1 - ytrain) * np.log(1 - _as[numLayers-1] + epsilon))
    closs = np.average(c1 + c2) * -1

    losses.append(closs)
    xaxis.append(i)

    # Backward propagation
    for id in range(numLayers):
        ix = numLayers - id - 1

        if ix == numLayers-1:
            dz = _as[ix] - ytrain
            dw = np.dot(dz, _as[ix-1].T)
            db = np.sum(dz, axis=1, keepdims=True) / m
            _dzs[ix] = dz
            _dws[ix] = dw
            _dbs[ix] = db

        elif ix == 0:
            dz = np.multiply(np.dot(Ws[ix+1].T, _dzs[ix+1]), relup(_zs[ix]))
            dw = np.dot(dz, X.T)
            db = np.sum(dz, axis=1, keepdims=True) / m
            _dzs[ix] = dz
            _dws[ix] = dw
            _dbs[ix] = db
        else:
            dz = np.multiply(np.dot(Ws[ix + 1].T, _dzs[ix + 1]), relup(_zs[ix]))
            dw = np.dot(dz, _as[ix-1].T)
            db = np.sum(dz, axis=1, keepdims=True) / m
            _dzs[ix] = dz
            _dws[ix] = dw
            _dbs[ix] = db

    # Update parameters
    for ix in range(numLayers):
        # print("Update parameters : " + str(ix))
        Ws[ix] = Ws[ix] - (alpha * _dws[ix])
        bs[ix] = bs[ix] - (alpha * _dbs[ix])

    # break

# Plot the losses
plt.plot(xaxis, losses)
plt.show()