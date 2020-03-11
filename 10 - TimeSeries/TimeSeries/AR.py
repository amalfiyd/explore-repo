import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf

df = pd.read_csv('datasets\\daily-min-temperatures.csv', index_col=0, parse_dates=[0], infer_datetime_format=True)
df.plot()
plt.show()

model = AutoReg(df.values, lags=1)
result = model.fit()
print('AR p:', result.ar_lags)

fig, (ax1,ax2) = plt.subplots(nrows=2)
# ax1.set_ylim([-1, 1])
# ax2.set_ylim([-1, 1])

plot_pacf(df.values, lags=60, ax=ax1, method='ols')
plot_acf(df.values, lags=60, ax=ax2)
plt.show()

#
# plot_acf(df.values, lags=60, ax=ax1)
# plot_pacf(df.values, lags=60, ax=ax2)
# # plt.show()
#
# # Create time different of 12
# df.columns = ['T_i']
# df['T_i-12'] = df['T_i'].shift(12)
# df['diff'] = df['T_i'] - df['T_i-12']
# # df['diff'].plot()
# # plt.show()
#
# # Plot PACF difference
# df = df.iloc[12:]
# plot_pacf(df['diff'], lags=60, ax=ax3)
#
# plt.show()
