import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.api import arma_generate_sample
from statsmodels.tsa.seasonal import seasonal_decompose

filename = r'C:\Users\amalf\Desktop\TimeSeries\datasets\airline-passengers.csv'
df = pd.read_csv(filename, parse_dates=[0], index_col=0, infer_datetime_format=True)

# Plot the timeseries for visualization
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
df.plot(ax=ax1)

# Plot acf and pacf
plot_acf(df, ax=ax2, lags=30)
plot_pacf(df, ax=ax3, lags=30)

# Show plot
plt.show()

# Testing for stationarity formally
from statsmodels.stats.stattools import jarque_bera
from statsmodels.tsa.stattools import adfuller, kpss

# We always want stationarity
# adfuller, h0: unit root is present, need to reject --> p-values need to be small
result = adfuller(df, maxlag=30)
print("p-value from adfuller", result[1]) # Support h0, non stationary process

# kpss, h0: unit root is not present, need to support --> p-values need to be large
result2 = kpss(df)
print("p-value from kpss", result2[1]) # Reject h0, non stationary process

# Once it is know to be unstationary process, trying transformation
# # diff transform
# df_temp = df.copy()
# for i in range(3):
#     df_temp = df_temp.diff()
#     df_temp.plot()
#     plt.show()

# # sqrt transform
# df_sqrt = np.sqrt(df)
# df_sqrt.plot()
# plt.show()
#
# # log transform
# df_sqrt = np.log(df)
# df_sqrt.plot()
# plt.show()

# # box cox transform
# from scipy.stats import boxcox
# df_bc, lmbd = boxcox(df.Passengers)
# plt.plot(df_bc)
# plt.show()

# Fitting SARIMAX


