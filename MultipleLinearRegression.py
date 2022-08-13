#################### Multiple Linear Regression ###################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import pylab as pl



df = pd.read_excel('Weather-V1.xlsx')
cdf = df[['Average','FM','SDK','VPM','PM','UPM','TMK','TXK','TNK']]


# Creation of data for train and test

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

# Multiple Regression Model

regr = linear_model.LinearRegression()
x = np.asanyarray(train[['FM','SDK','VPM','PM','UPM','TMK','TXK','TNK']])
y = np.asanyarray(train[['Average']])
regr.fit (x, y)
# The coefficients
print ('Coefficients: ', regr.coef_)


# Prediction

y_hat= regr.predict(test[['FM','SDK','VPM','PM','UPM','TMK','TXK','TNK']])
x = np.asanyarray(test[['FM','SDK','VPM','PM','UPM','TMK','TXK','TNK']])
y = np.asanyarray(test[['Average']])
print("Residual sum of squares: %.2f"
      % np.mean((y_hat - y) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x, y))


# Plot each of the columns in terms of "Average"


plt.scatter(cdf.FM, cdf.Average,  color='blue')
plt.xlabel("FM")
plt.ylabel("Average")
plt.show()

plt.scatter(cdf.SDK, cdf.Average,  color='blue')
plt.xlabel("SDK")
plt.ylabel("Average")
plt.show()


#VPM can be a relative good predictor

plt.scatter(cdf.VPM, cdf.Average,  color='blue')
plt.xlabel("VPM")
plt.ylabel("Average")
plt.show()

plt.scatter(cdf.PM, cdf.Average,  color='blue')
plt.xlabel("PM")
plt.ylabel("Average")
plt.show()

plt.scatter(cdf.UPM, cdf.Average,  color='blue')
plt.xlabel("UPM")
plt.ylabel("Average")
plt.show()

#TMK can be a relative good predictor

plt.scatter(cdf.TMK, cdf.Average,  color='blue')
plt.xlabel("TMK")
plt.ylabel("Average")
plt.show()

#TXK can be a relative good predictor

plt.scatter(cdf.TXK, cdf.Average,  color='blue')
plt.xlabel("TXK")
plt.ylabel("Average")
plt.show()

#TNK can be a relative good predictor

plt.scatter(cdf.TNK, cdf.Average,  color='blue')
plt.xlabel("TNK")
plt.ylabel("Average")
plt.show()

