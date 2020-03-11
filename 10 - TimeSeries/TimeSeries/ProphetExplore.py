import pandas as pd
import numpy as np
import os
import datetime
import matplotlib.pyplot as plt
from fbprophet import Prophet


rootdir = r'datasets'
filename = os.path.join(rootdir, 'example_wp_log_peyton_manning.csv')

df = pd.read_csv(filename)

# Fitting data into dataframe
m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=365)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

forecast.plot()
plt.show()
