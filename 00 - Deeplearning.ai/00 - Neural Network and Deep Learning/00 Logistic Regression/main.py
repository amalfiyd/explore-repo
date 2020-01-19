import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

# Helper
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Input Variables
dataset = load_breast_cancer()
m = dataset.data.shape[0]
nFeat = dataset.data.shape[1]

Xtrain_ = dataset.data
Xtrain = Xtrain_ / np.max(Xtrain_)
ytrain = dataset.target.reshape(m, 1)
epsilon = 1e-5

# Random Setup W and b
W = np.random.rand(nFeat, 1)
b = np.random.rand(1, 1)

# Training
numIter = 100
alpha = 0.00001

losses = []
xaxis = [x for x in range(numIter)]

for i in range(numIter):
    print("Running iteration " + str(i))

    # z = WX + b
    z1 = np.dot(Xtrain, W)
    z = np.add(z1, b)

    # a = sigmoid(z)
    yhat = sigmoid(z)

    # L_yhaty = -((ytrain log yhat) + ((1-y) log (1-yhat)))
    c1 = (ytrain.reshape(m, 1) + epsilon) * np.log(yhat + epsilon)
    c2 = (1 - (ytrain.reshape(m, 1) + epsilon) * np.log(1 - yhat + epsilon))
    L_yhaty = (c1 + c2)

    # Current total loss
    ci_loss = 1/m * np.sum(L_yhaty)
    losses.append(ci_loss)
    print("Current iter total loss: " + str(ci_loss))

    # da = (np.divide(-y, a)) + (np.divide(1-ytrain.reshape(10,1), 1-a))
    c1 = -1 * np.divide(ytrain.reshape(m, 1), yhat)
    c2 = np.divide(1 - ytrain.reshape(m, 1), 1 - yhat)
    da = c1 + c2

    # dz = a - y
    dz = yhat - ytrain.reshape(m, 1)

    # dW = x * dz
    # db = dz
    dW = np.dot(Xtrain.reshape(nFeat, m), dz)
    db = dz

    # Update parameter
    W = W - (alpha * dW)
    b = b - (alpha * db)

    # variable = input('Press enter!')
    # break

# Plotting losses
plt.plot(xaxis, losses)
plt.show()

