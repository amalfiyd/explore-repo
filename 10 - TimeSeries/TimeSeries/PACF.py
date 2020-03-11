import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('datasets\data.csv', skiprows=1, index_col=0, infer_datetime_format=True)
df.columns = ['T_i']

# Creating shifts
SHIFTS = 2
for i in range(1, SHIFTS+1):
    df['T_i-'+str(i)] = df['T_i'].shift(i)

# Dropping 1st 2 indexes
df = df.iloc[SHIFTS:]

# Creating linear model T_i|T_i-1
df_X = df[['T_i-1']]
df_y = df['T_i']
lm = linear_model.LinearRegression()
model = lm.fit(df_X, df_y)
df['Predicted_T_i|T_i-1'] = lm.predict(df_X)
df['Residual_T_i|T_i-1'] = df['T_i'] - df['Predicted_T_i|T_i-1']

# Creating linear model T_i-2|T_i-1
df_X = df[['T_i-1']]
df_y = df['T_i-2']
lm = linear_model.LinearRegression()
model = lm.fit(df_X, df_y)
df['Predicted_T_i-2|T_i-1'] = lm.predict(df_X)
df['Residual_T_i-2|T_i-1'] = df['T_i-2'] - df['Predicted_T_i-2|T_i-1']

# Comparing statsmodels pacf and calculation
from statsmodels.tsa.stattools import pacf

pacf_val = pacf(df['T_i'], nlags=2)
calculated_val = df[['Residual_T_i|T_i-1', 'Residual_T_i-2|T_i-1']].corr()
