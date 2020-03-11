import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from pandas.plotting import lag_plot, autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import acf, pacf
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AR

# Importing dataset
rootdir = r'C:\Users\amalf\Desktop\TimeSeries'
datasetsdir = os.path.join(rootdir, 'datasets')
filename = os.path.join(datasetsdir, 'daily-min-temperatures.csv')

# Load to memory and plot
temp_s = pd.read_csv(filename, header=0, index_col=0)

# Train and test
X = temp_s.values
train, test = X[1: len(X)-7], X[len(X)-7:]

# Train AR
model = AR(train)
model_fit = model.fit()
print('Lag: %s' % model_fit.k_ar)
print('Coefficients: %s' % model_fit.params)

# Make predictions
predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)

# plot results
plt.plot(test)
plt.plot(predictions, color='red')
plt.show()

# Automated AR selection
window = model.k_ar
coef = model_fit.params

history = train[len(train)-window:]
history = [history[i] for i in range(len(history))]
predictions = list()

for t in range(len(test)):
    length = len(history)
    lag = [history[i] for i in range(length-window,length)]
    yhat = coef[0]
    for d in range(window):
        yhat += coef[d+1] * lag[window-d-1]
    obs = test[t]
    predictions.append(yhat)
    history.append(obs)
    print('predicted=%f, expected=%f' % (yhat, obs))

error = mean_squared_error(test, predictions)


