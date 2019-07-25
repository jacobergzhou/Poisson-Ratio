# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:33:17 2019

@author: liubeisong
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Poisson_data_no_metal_07192019.csv')
X = dataset.iloc[:,6:187].values
y = dataset.iloc[:,189].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

plt.plot(y_pred, y_test, 'ro')
plt.axis([0,0.5,0,0.5])
plt.plot([0,0.1,0.2,0.3,0.4,0.5],[0,0.1,0.2,0.3,0.4,0.5])

