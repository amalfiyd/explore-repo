from tsplot import tsplot
from statsmodels.tsa.api import arma_generate_sample
from statsmodels.tsa.api import ARMA
from statsmodels.tsa.arima_model import ARIMA

import numpy as np
import matplotlib.pyplot as plt

# Simulate ARCH(1) series
# Var(yt) = a_0 + a_1*y{t-1}**2
# if a_1 is between 0 and 1 then yt is white noise
np.random.seed(13)

a0 = 2
a1 = .5

y = w = np.random.normal(size=1000)
Y = np.empty_like(y)

for t in range(len(y)):
    y[t] = w[t] * np.sqrt((a0 + a1*y[t-1]**2))

# simulated ARCH(1) series, looks like white noise
tsplot(y, lags=30)
plt.show()

tsplot(np.power(y,2), lags=30)
plt.show()