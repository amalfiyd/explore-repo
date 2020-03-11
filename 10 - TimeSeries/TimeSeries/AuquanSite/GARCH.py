from tsplot import tsplot
from statsmodels.tsa.api import arma_generate_sample
from statsmodels.tsa.api import ARMA
from statsmodels.tsa.arima_model import ARIMA

import numpy as np
import matplotlib.pyplot as plt

# Simulating a GARCH(1, 1) process
np.random.seed(2)
a0 = 0.2
a1 = 0.5
b1 = 0.3

n = 10000
w = np.random.normal(size=n)
eps = np.zeros_like(w)
sigsq = np.zeros_like(w)

for i in range(1, n):
    sigsq[i] = a0 + a1*(eps[i-1]**2) + b1*sigsq[i-1]
    eps[i] = w[i] * np.sqrt(sigsq[i])

_ = tsplot(eps, lags=30)
plt.show()

_ = tsplot(eps**2, lags=30)
plt.show()

# Fit a GARCH(1, 1) model to our simulated EPS series
# We use the arch_model function from the ARCH package
from arch import arch_model
am = arch_model(eps)
res = am.fit(update_freq=5)
print(res.summary())
