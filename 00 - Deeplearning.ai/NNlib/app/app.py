"""
Filename    : app.py
Desc        : Contains the main application runtime of NNlib
"""

from NNlib.nncorelib.Network import Network
from sklearn import datasets
import numpy as np
import pandas as pd
import h5py

filename = r'NNlib/app/train_catvnoncat.h5'
f = h5py.File(filename, 'r+')
Xtrain = np.array(f['train_set_x'][:])
Xtrain = Xtrain.reshape(Xtrain.shape[0], -1).T
Xtrain_norm = Xtrain / 255.

m = Xtrain_norm.shape[1]
nFeat = Xtrain_norm.shape[0]

ytrain = np.array(f['train_set_y'][:])
ytrain = ytrain.reshape(1, m)

nClass = len(np.unique(ytrain))

# Hyper parameters selection
nLayers = 10
epoch = 500
alpha = 0.03
randConst = 0.001
nodesL = 20
actFunct = "relu"

myNN = Network(nLayers, epoch, alpha, Xtrain, ytrain, nClass, actFunct, randConst, nodesL)
myNN.train()
myNN.plot()
