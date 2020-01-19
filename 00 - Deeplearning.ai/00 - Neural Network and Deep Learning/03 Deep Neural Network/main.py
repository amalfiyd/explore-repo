import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Functions and Helpers
# Activation functions and derivatives
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

# Propagations
def forwardProp(l, WL, bL, aL, activations):
    z = np.dot(WL[l], aL[l-1]) + bL[l]
    a = activation(z, activations[l])
    return (z, a)

def backwardProp(l, WL, bL, aL, dWL, dbL, daL, activations):
    dz = np.multiply(daL[l], activationp(zL[l], activations[l]))
    dw = 1/m * np.dot(dz, aL[l-1].T)
    db = 1/m * np.sum(dz, axis=1, keepdims=True)
    dalm1 = np.dot(WL[l].T, dz)
    return (dz, dw, db, dalm1)

def activation(z, act="relu"):
    if act == "relu":
        return relu(z)
    elif act == "sigmoid":
        return sigmoid(z)
    elif act == "tanh":
        return tanh(z)
    else:
        return lrelu(z)

def activationp(z, act="relu"):
    if act == "relu":
        return relup(z)
    elif act == "sigmoid":
        return sigmoidp(z)
    elif act == "tanh":
        return tanhp(z)
    else:
        return lrelup(z)

def calc_daL(a, ytrain):
    return -1 * (np.divide(ytrain, a)) + (np.divide(1-ytrain, 1-a))

def loss(ytrain, a, epsilon=1e-5):
    c1 = ytrain * np.log(a + epsilon)
    c2 = ((1 - ytrain) * np.log(1 - a + epsilon))
    return (c1, c2, -1/m * np.sum(c1 + c2))

# Dataset Preparation
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

m = Xtrain_norm.shape[1]
nFeat = Xtrain_norm.shape[0]

# Hyperparameters
L = 10
WL = {}                 # == L
bL = {}                 # == L
aL = {
    0: Xtrain_norm
}              # == L + 1
nL = {
    0: nFeat,
    1: 5,
    2: 5,
    3: 5,
    4: 5,
    5: 5,
    6: 5,
    7: 5,
    8: 5,
    9: 3,
    10: 1,
}              # == L + 1
zL = {}                 # == L
activations = {
    1: 'lrelu',
    2: 'lrelu',
    3: 'lrelu',
    4: 'lrelu',
    5: 'lrelu',
    6: 'lrelu',
    7: 'lrelu',
    8: 'lrelu',
    9: 'lrelu',
    10: 'sigmoid',
}     # == L
epoch = 5000
alpha = 3e-2
randomizeConst = 0.001

# Cache Variables
daL = {}
dzL = {}
dWL = {}
dbL = {}
losses = []
xaxis = []

# Parameters initialization
for l in range(L):
    WL[l+1] = np.random.randn(nL[l+1], nL[l]) * randomizeConst
    bL[l+1] = np.zeros((nL[l+1], 1))

for iter in range(epoch):
    print("Running epoch : " + str(iter))

    # Forward Propagation
    for l_ in range(L):
        l = l_ + 1
        z, a = forwardProp(l, WL, bL, aL, activations)
        zL[l] = z
        aL[l] = a

    # Loss
    c1, c2, closs = loss(ytrain, aL[L])
    losses.append(closs)
    xaxis.append(iter)

    # Backpropagation
    daL[L] = calc_daL(a, ytrain)
    for l_ in range(L):
        l = L - l_
        dzL[l], dWL[l], dbL[l], daL[l-1] = backwardProp(l, WL, bL, aL, dWL, dbL, daL, activations)

    # Update parameters
    for l_ in range(L):
        l = l_ + 1
        WL[l] = WL[l] - (alpha * dWL[l])
        bL[l] = bL[l] - (alpha * dbL[l])

plt.plot(xaxis, losses)
plt.show()