# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values
y = dataset.iloc[:, 3].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#find num clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init= 'k-means++', max_iter = 300, n_init = 10, random_state =0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11), wcss)

#apply num clus = 5
kmeans = KMeans(n_clusters = 5, init= 'k-means++', max_iter = 300, n_init = 10, random_state =0)
y_kmeans = kmeans.fit_predict(X)

#visualize
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s =100, c = 'red', label = 'clus0')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s =100, c = 'blue', label = 'clus1')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s =100, c = 'green', label = 'clus2')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s =100, c = 'black', label = 'clus3')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s =100, c = 'orange', label = 'clus4')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s =300, c = 'magenta', label = 'centroids')
plt.title('clusters')
plt.show()

