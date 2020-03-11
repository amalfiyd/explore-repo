import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from pandas.plotting import lag_plot, autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error

# Importing dataset
rootdir = r'C:\Users\amalf\Desktop\TimeSeries'
datasetsdir = os.path.join(rootdir, 'datasets')
filename = os.path.join(datasetsdir, 'daily-min-temperatures.csv')

# Load to memory and plot
temp_s = pd.read_csv(filename, header=0, index_col=0)
temp_s.plot()
plt.show()

# Lag plot
lag_plot(temp_s)
plt.show()

# Checking correlation matrix
values = pd.DataFrame(temp_s.values)
temp_df = pd.concat([values.shift(1), values], axis=1)
temp_df.columns = ['t-1', 't']

# Checking autocorrelation - pandas
# autocorrelation_plot(temp_s)
# plt.show()

# Checking autocorrelation - statsmodel
plot_acf(temp_s, lags=7)
plt.show()

plot_pacf(temp_s, lags=7)
plt.show()

# Testing prediction walk-forward
X = temp_df.values
train, test = X[1:len(X)-7], X[len(X)-7:]
train_X, train_y = train[:,0], train[:,1]
test_X, test_y = test[:,0], test[:,1]

def model_persistence(x):
    return x

# Walk-forward validation
predictions = []
for x in test_X:
    yhat = model_persistence(x)
    predictions.append(yhat)
test_score = mean_squared_error(test_y, predictions)
print("Test MSE: %.3f" % test_score)
plt.plot(test_y)
plt.plot(predictions)
