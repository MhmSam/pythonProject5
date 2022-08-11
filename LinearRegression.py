################### Multiple Linear Regression ###################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import pylab as pl


df = pd.read_csv("Last_Wetter_1.csv")
cdf = df[['Mittelwert', 'W_mean','S','Dampf_mean','Luft_d_mean','F_mean' , 'T_mean' , 'T_max' , 'T_min']]


# Plot each of the columns in terms of "Mittelwert"

plt.scatter(cdf.W_mean, cdf.Mittelwert,  color='blue')
plt.xlabel("W_mean")
plt.ylabel("Mittelwert")
plt.show()

plt.scatter(cdf.S, cdf.Mittelwert,  color='blue')
plt.xlabel("S")
plt.ylabel("Mittelwert")
plt.show()

plt.scatter(cdf.Dampf_mean, cdf.Mittelwert,  color='blue')
plt.xlabel("Dampf_mean")
plt.ylabel("Mittelwert")
plt.show()

plt.scatter(cdf.Luft_d_mean, cdf.Mittelwert,  color='blue')
plt.xlabel("Luft_d_mean")
plt.ylabel("Mittelwert")
plt.show()


plt.scatter(cdf.F_mean, cdf.Mittelwert,  color='blue')
plt.xlabel("F_mean")
plt.ylabel("Mittelwert")
plt.show()

plt.scatter(cdf.T_mean, cdf.Mittelwert,  color='blue')
plt.xlabel("T_mean")
plt.ylabel("Mittelwert")
plt.show()

plt.scatter(cdf.T_max, cdf.Mittelwert,  color='blue')
plt.xlabel("T_max")
plt.ylabel("Mittelwert")
plt.show()


plt.scatter(cdf.T_min, cdf.Mittelwert,  color='blue')
plt.xlabel("T_min")
plt.ylabel("Mittelwert")
plt.show()

# Separation of data for training and testing

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

# Multiple Regression Model

regr = linear_model.LinearRegression()
x = np.asanyarray(train[['W_mean','S','Dampf_mean','Luft_d_mean','F_mean' , 'T_mean' , 'T_max' , 'T_min']])
y = np.asanyarray(train[['Mittelwert']])
regr.fit (x, y)
# The coefficients
print ('Coefficients: ', regr.coef_)

# Prediction

y_hat= regr.predict(test[['W_mean','S','Dampf_mean','Luft_d_mean','F_mean' , 'T_mean' , 'T_max' , 'T_min']])
x = np.asanyarray(test[['W_mean','S','Dampf_mean','Luft_d_mean','F_mean' , 'T_mean' , 'T_max' , 'T_min']])
y = np.asanyarray(test[['Mittelwert']])
print("Residual sum of squares: %.2f"
      % np.mean((y_hat - y) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x, y))


