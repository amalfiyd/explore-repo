import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

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
dataset = load_breast_cancer()
Xtrain_ = dataset.data
Xtrain = np.divide(Xtrain_, np.max(Xtrain_))

m = Xtrain.shape[0]
inputFeat = Xtrain.shape[1]
ytrain = dataset.target.reshape(m, 1)

# Hyperparameters
numIter = 1000
layers = [inputFeat, 4, 3, 1]
learningRate = 0.0003

# Initialization of parameters
Ws = []
Bs = []
dWs = []
dBs = []
_as = []
dzs = []
for layer in range(len(layers)-1):
    w_temp = np.random.rand(layers[layer+1], layers[layer])
    b_temp = np.random.rand(layers[layer+1], m)
    a_temp = np.zeros((layers[layer+1], m))

    Ws.append(w_temp)
    Bs.append(b_temp)
    dWs.append([])
    dBs.append([])
    _as.append([])
    dzs.append([])

# Training Process
loss = []       # total losses tracker
xaxis = []      # xaxis of losses for plotting
epsilon = 1e-10  # epsilon for log function
for i in range(numIter):
    print("Iteration number : " + str(i))

    # Forward Propagation
    a = Xtrain
    _as[0] = a
    for layer in range(len(layers)-1):
        z_c = np.dot(a, Ws[layer].T)
        z = np.add(z_c, Bs[layer].T)
        # if not last layer
        if layer+1 < len(layers)-1:
            a = relu(z)
            _as[layer] = a
        # if last layer
        else:
            a = sigmoid(z)
            _as[layer] = a

    # Back Propagation
    for layer in range(len(layers)-1):
        aix = len(layers) - layer - 2
        if aix == len(layers) - 2:
            a_later = _as[aix]
            a_former = _as[aix-1]

            dz = a_later - ytrain
            dzs[aix] = dz

            dW_c = np.dot(dz.T, a_former)
            dW = np.divide(dW_c, m)
            dWs[aix] = dW

            db_c = np.sum(dz, axis=1, keepdims=True)
            db = np.divide(db_c, m)
            dBs[aix] = db

        else:
            dz_c1 = np.dot(dzs[aix+1], Ws[aix+1])
            dz_c2 = relup(_as[aix])
            dz = np.multiply(dz_c1, dz_c2)
            dzs[aix] = dz

            dW_c = np.dot(dz.T, _as[aix])
            dW = np.divide(dW_c, m)
            dWs[aix] = dW

            db_c = np.sum(dz, axis=1, keepdims=True)
            db = np.divide(db_c, m)
            dBs[aix] = db

    # Update Parameters
    for layer in range(len(layers)-1):
        Ws[layer] = Ws[layer] - (learningRate * dWs[layer])
        Bs[layer] = Bs[layer] - (learningRate * dBs[layer])

