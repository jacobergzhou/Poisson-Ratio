import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pd.read_csv('Non_metal_07252019.csv')
X = dataset.iloc[:,7:188].values
y = dataset.iloc[:,190].values

#linear regression

# lin_reg = LinearRegression()
# lin_reg.fit(X,y)
# pred = lin_reg.predict(X)
# print(y)
# print(pred)
# plt.plot(y,pred,'ro',markersize = 1)
# plt.axis([0,0.5,0,0.5])
# plt.plot([0,0.1,0.2,0.3,0.4,0.5],[0,0.1,0.2,0.3,0.4,0.5])
# plt.show()


#polynomial regression
poly_reg = PolynomialFeatures(degree = 3)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)
pred = lin_reg_2.predict(X_poly)

plt.plot(y,pred,'ro',markersize = 1)
plt.axis([0,0.5,0,0.5])
plt.plot([0,0.1,0.2,0.3,0.4,0.5],[0,0.1,0.2,0.3,0.4,0.5])
plt.show()




