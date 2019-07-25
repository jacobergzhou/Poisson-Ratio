# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Poisson_data_no_metal_07252019.csv')
X = dataset.iloc[0:4000,7:188].values
y = dataset.iloc[0:4000,190].values
X_test


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

pred = lin_reg.predict(X)
plt.plot(y,pred,'ro')
plt.axis([0,0.5,0,0.5])
plt.plot([0,0.1,0.2,0.3,0.4,0.5],[0,0.1,0.2,0.3,0.4,0.5])