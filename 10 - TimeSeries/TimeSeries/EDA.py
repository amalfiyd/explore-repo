import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.stattools import adfuller, kpss

rootdir = r'datasets'
filename = os.path.join(rootdir, 'data.csv')

date_parser = lambda x: datetime.datetime.strptime(x, '%Y%m')
df = pd.read_csv(filename, header=1, index_col=0, parse_dates=[0], date_parser=date_parser)
df['Diff'] = df['Value'].diff()

# Augmented dickey fuller test
result = adfuller(df.Value)
result2 = kpss(df.Value)

# # Rolling window
# ROLLMEAN = 50
# df['RollMean'] = df.Value.rolling(ROLLMEAN).mean()
# df.Value.plot()
# df.RollMean.plot()
# plt.show()

# # PACF and ACF
# fig, (ax0, ax1, ax2) = plt.subplots(3, 1)
# df.Value.plot(ax=ax0)
# plot_acf(df.Value, ax=ax1)
# plot_pacf(df.Value, ax=ax2)
# plt.show()


