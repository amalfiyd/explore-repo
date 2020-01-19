"""
Filename    : Activation.py
Desc        : Contains list of activation functions for NN
"""

import numpy as np

class Function:
    def __init__(self, act="relu"):
        self.act = act
        self.actp = act+"p"

    def activate(self, z):
        act = self.act
        if act == "relu":
            return self.relu(z)
        elif act == "sigmoid":
            return self.sigmoid(z)
        elif act == "tanh":
            return self.tanh(z)
        else:
            return self.lrelu(z)

    def activatep(self, z):
        act = self.act
        if act == "relu":
            return self.relup(z)
        elif act == "sigmoid":
            return self.sigmoidp(z)
        elif act == "tanh":
            return self.tanhp(z)
        else:
            return self.lrelup(z)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoidp(self, x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))

    def tanh(self, x):
        return np.tanh(x)

    def tanhp(self, x):
        return 1 - np.power(self.tanh(x), 2)

    def relu(self, x):
        return np.maximum(0, x)

    def relup(self, x):
        return np.where(x > 0, 1.0, 0.0)

    def lrelu(self, x):
        return np.maximum(0.01 * x, x)

    def lrelup(self, x):
        return np.where(x > 0, 1.0, 0.01)

    def softmax(self, x):
        x -= np.max(x)
        sm = (np.exp(x).T / np.sum(np.exp(x), axis=1)).T
        return sm