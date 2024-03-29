# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:05:48 2019

@author: Sowmitha
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:39:16 2019

@author: Sowmitha
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
#imputer = imputer.fit(X[:, 1:3])
#X[:, 1:3] = imputer.transform(X[:, 1:3])

#from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#labelencoder_X = LabelEncoder()
#X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
#onehotencoder = OneHotEncoder(categorical_features = [0])
#X = onehotencoder.fit_transform(X).toarray()

#labelencoder_y = LabelEncoder()
#y = labelencoder_y.fit_transform(y)
"""
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size = 0.2, 
                                                     random_state = 0)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""



from sklearn.linear_model import LinearRegression
lin_model = LinearRegression()
lin_model.fit(X, y)


from sklearn.preprocessing import PolynomialFeatures
poly_model = PolynomialFeatures(degree =4)
X_poly = poly_model.fit_transform(X)
lin_model_poly = LinearRegression()
lin_model_poly.fit(X_poly,y)


X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y)
plt.plot(X, lin_model.predict(X), color='green')
plt.plot(X_grid, lin_model_poly.predict(poly_model.fit_transform(X_grid)), color='red')
plt.show()

lin_model.predict([[6.5]])
#y_poly_pred = lin_model_poly.predict(6.5)
lin_model_poly.predict(poly_model.fit_transform([[6.5]]))
