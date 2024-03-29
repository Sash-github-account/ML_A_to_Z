# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:16:25 2019

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

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

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

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size = 1/3, 
                                                     random_state = 0)
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('salary Vs exp (training)')
plt.xlabel('years of exp')
plt.ylabel('salary')
plt.show()


plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('salary Vs exp (test)')
plt.xlabel('years of exp')
plt.ylabel('salary')
plt.show()


