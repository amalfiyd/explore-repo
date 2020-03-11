from tsplot import tsplot
from statsmodels.tsa.api import arma_generate_sample
from statsmodels.tsa.api import ARMA
from statsmodels.tsa.arima_model import ARIMA

import numpy as np
import matplotlib.pyplot as plt

# Set experiment variables
np.random.seed(1)

# Simulate an ARIMA(2,1,1) model with alphas=[0.5,-0.25] and betas=[-0.5]
max_lag = 30
n = int(5000)
burn = 2000

alphas = np.array([0.5, -0.25])
betas = np.array([-0.5])

ar = np.r_[1, -alphas]
ma = np.r_[1, betas]

arma21 = arma_generate_sample(ar=ar, ma=ma, nsample=n, burnin=burn)
arima211 = np.diff(arma21)
_ = tsplot(arima211, lags=max_lag)
plt.show()

# Fit ARIMA(p, d, q) model
# pick best order and final model based on aic

best_aic = np.inf
best_order = None
best_mdl = None

# Estimating the order of ARIMA based on AIC
pq_rng = range(5) # [0,1,2,3]
d_rng = range(2) # [0,1]
for i in pq_rng:
    for d in d_rng:
        for j in pq_rng:
            try:
                tmp_mdl = ARIMA(arima211, order=(i, d, j)).fit(method='mle', trend='nc')
                tmp_aic = tmp_mdl.aic
                if tmp_aic < best_aic:
                    best_aic = tmp_aic
                    best_order = (i, d, j)
                    best_mdl = tmp_mdl
            except:
                continue


print('aic: %6.5f | order: %s'%(best_aic, best_order))

# ARIMA model resid plot
_ = tsplot(best_mdl.resid, lags=30)
plt.show()

# Check ljungbox test
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.stats.stattools import jarque_bera
print("Ljung-Box test: ", acorr_ljungbox(best_mdl.resid, lags=[30], boxpierce=False))

# Check jarque bera
score, pvalue, _, _ = jarque_bera(best_mdl.resid)
print('Jarque Bera test p value: ', pvalue)

# Create a 21 day forecast of SPX returns with 95%, 99% CI
import pandas as pd

n_steps = 100
f, err95, ci95 = best_mdl.forecast(steps=n_steps) # 95% CI
_, err99, ci99 = best_mdl.forecast(steps=n_steps, alpha=0.01) # 99% CI

# idx = pd.date_range(arima211.index[-1], periods=n_steps, freq='D')
# fc_95 = pd.DataFrame(np.column_stack([f, ci95]),
#                      index=idx, columns=['forecast', 'lower_ci_95', 'upper_ci_95'])
# fc_99 = pd.DataFrame(np.column_stack([ci99]),
#                      index=idx, columns=['lower_ci_99', 'upper_ci_99'])
# fc_all = fc_95.combine_first(fc_99)
# fc_all.head()

temp = np.concatenate([arima211, f])
plt.plot(f)
plt.show()
