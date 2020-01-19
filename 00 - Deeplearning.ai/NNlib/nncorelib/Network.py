"""
Filename    : Network.py
Desc        : Contains the main engine of NNlib
"""
import numpy as np
import NNlib.nncorelib.Activation as act
import matplotlib.pyplot as plt

class Network:
    def __init__(self, nLayers, epoch, alpha, Xtrain, ytrain, nClass, actFunct="relu", randConst=0.001, nodesL=5, lossEps=1e-5):
        # Hyper parameters
        self.nLayers = nLayers
        self.epoch = epoch
        self.alpha = alpha
        self.Xtrain = Xtrain
        self.ytrain = ytrain
        self.nFeat = self.Xtrain.shape[0]
        self.nClass = nClass
        self.mTrain = self.Xtrain.shape[1]
        self.randConst = randConst
        self.nodesL = nodesL
        self.actFunct = actFunct
        self.lossEps = lossEps

        # Parameters
        self.nL = {}
        self.WL = {}
        self.bL = {}
        self.aL = {}
        self.zL = {}
        self.activations = {}
        self.losses = []
        self.axis = []

        # Cache Parameters
        self.daL = {}
        self.dzL = {}
        self.dWL = {}
        self.dbL = {}

        # Initializing Parameters
        self.init_param()

    def init_param(self):
        # Init nL
        self.nL[0] = self.nFeat
        for i in range(self.nLayers-1):
            self.nL[i+1] = self.nodesL
        self.nL[self.nLayers] = 1 if self.nClass <= 2 else self.nClass

        # Init WL and bL
        for l in range(self.nLayers):
            self.WL[l + 1] = np.random.randn(self.nL[l + 1], self.nL[l]) * self.randConst
            self.bL[l + 1] = np.zeros((self.nL[l + 1], 1))

        # Init activations
        for i in range(self.nLayers-1):
            self.activations[i + 1] = self.actFunct
        self.activations[self.nLayers] = "sigmoid" if self.nClass <= 2 else "softmax"

        # Init aL
        self.aL[0] = self.Xtrain

    def forwardProp(self, l):
        z = np.dot(self.WL[l], self.aL[l-1]) + self.bL[l]
        actFunct = act.Function(self.activations[l])
        a = actFunct.activate(z)
        self.zL[l] = z
        self.aL[l] = a

    def calcLoss(self):
        c1 = self.ytrain * np.log(self.aL[self.nLayers] + self.lossEps)
        c2 = ((1 - self.ytrain) * np.log(1 - self.aL[self.nLayers] + self.lossEps))
        loss = -1 / self.mTrain * np.sum(c1 + c2)
        self.losses.append(loss)
        self.axis.append(len(self.losses)-1)

    def daLAtnLayers(self):
        self.daL[self.nLayers] = -1 * (np.divide(self.ytrain, self.aL[self.nLayers])) + (np.divide(1-self.ytrain, 1-self.aL[self.nLayers]))

    def backProp(self, l):
        actFunct = act.Function(self.activations[l])

        dz = np.multiply(self.daL[l], actFunct.activatep(self.zL[l]))
        dw = 1 / self.mTrain * np.dot(dz, self.aL[l - 1].T)
        db = 1 / self.mTrain * np.sum(dz, axis=1, keepdims=True)
        dalm1 = np.dot(self.WL[l].T, dz)
        self.dzL[l] = dz
        self.dWL[l] = dw
        self.dbL[l] = db
        self.daL[l-1] = dalm1

    def updateParams(self, l):
        self.WL[l] = self.WL[l] - (self.alpha * self.dWL[l])
        self.bL[l] = self.bL[l] - (self.alpha * self.dbL[l])

    def runEpoch(self):
        for l_ in range(self.nLayers):
            l = l_ + 1
            self.forwardProp(l)

        self.calcLoss()

        self.daLAtnLayers()

        for l_ in range(self.nLayers):
            l = self.nLayers - l_
            self.backProp(l)

        for l_ in range(self.nLayers):
            l = l_ + 1
            self.updateParams(l)

    def train(self):
        for i in range(self.epoch):
            if i % 100 == 0:
                print("Running on epoch #"+str(i))
            self.runEpoch()

    def plot(self):
        plt.plot(self.axis, self.losses)
        plt.show()







