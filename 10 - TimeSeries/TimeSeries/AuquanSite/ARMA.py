from tsplot import tsplot
from statsmodels.tsa.api import arma_generate_sample
from statsmodels.tsa.api import ARMA

import numpy as np
import matplotlib.pyplot as plt

# Set experiment variables
np.random.seed(1)

# # Part 1
# # Simulate an ARMA(2, 2) model with alphas=[0.5,-0.25] and betas=[0.5,-0.3]
# max_lag = 30
# n = int(5000) # lots of samples to help estimates
# burn = int(n/10) # number of samples to discard before fit
#
# alphas = np.array([0.5, -0.3])
# betas = np.array([0.5, -0.3])
# ar = np.r_[1, -alphas]
# ma = np.r_[1, betas]
# #
# # ar = [1, 0.]
# # ma = [1, 0.]
#
# # Generate ARMA(2, 2)
# arma22 = arma_generate_sample(ar=ar, ma=ma, nsample=n, burnin=burn)
# _ = tsplot(arma22, lags=max_lag)
# plt.show()
#
# # # Test model with cheat
# # mdl = ARMA(arma22, order=(2, 2)).fit(maxlag=max_lag, method="mle", trend='nc', burnin=burn)
# # print(mdl.summary())

# Part 2
# Simulate an ARMA(3, 2) model with alphas=[0.5,-0.4,0.25] and betas=[0.5,-0.3]
max_lag = 30
n = int(5000)
burn = 2000

alphas = np.array([0.5, -0.4, 0.25])
betas = np.array([0.5, -0.3])

ar = np.r_[1, -alphas]
ma = np.r_[1, betas]

arma32 = arma_generate_sample(ar=ar, ma=ma, nsample=n, burnin=burn)
_ = tsplot(arma32, lags=max_lag)
plt.show()

# Estimate by grid search using AIC
# pick best order by aic
# smallest aic value wins
best_aic = np.inf
best_order = None
best_mdl = None
rng = range(5)
for i in rng:
    for j in rng:
        try:
            print(i, '--', j)
            tmp_mdl = ARMA(arma32, order=(i, j)).fit(method='mle', trend='nc')
            tmp_aic = tmp_mdl.aic
            if tmp_aic < best_aic:
                best_aic = tmp_aic
                best_order = (i, j)
                best_mdl = tmp_mdl
        except:
            continue

print('aic: %6.5f | order: %s'%(best_aic, best_order))

# Checking residuals if white noise or not
from statsmodels.stats.diagnostic import acorr_ljungbox
print(acorr_ljungbox(best_mdl.resid, lags=[30], boxpierce=False))
_ = tsplot(best_mdl.resid, lags=max_lag)
plt.show()

