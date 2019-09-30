# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:04:52 2019

@author: Sashwath
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Social_network_Ads.csv')
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, 4].values

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

#split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size = 0.25, 
                                                     random_state = 0)
#scale
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#fit model


#predict
y_pred = classifier.predict(X_test)

count =0
tot = 0
for i in range(len(y_test)):
    tot += 1
    if(y_pred[i] == y_test[i]):
        count += 1
        
acc = count/tot

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#visualize
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

