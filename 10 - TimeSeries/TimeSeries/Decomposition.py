from statsmodels.tsa.seasonal import seasonal_decompose

import pandas as pd
import matplotlib.pyplot as plt

ts = pd.read_csv(r'datasets\airline-passengers.csv', index_col=0, parse_dates=[0])

# try to decompose
result = seasonal_decompose(ts, model='additive')
result.plot()
plt.show()

result2 = seasonal_decompose(ts, model='multiplicative')
result2.plot()
plt.show()