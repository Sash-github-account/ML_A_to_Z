# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

#find optimal num clusters
import scipy.cluster.hierarchy as sch
dend = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('dendro')
plt.xlabel('cust')
plt.ylabel('Euc dist')
plt.show()

# fit model
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

#visualize
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s =100, c = 'red', label = 'clus0')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s =100, c = 'blue', label = 'clus1')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s =100, c = 'green', label = 'clus2')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s =100, c = 'black', label = 'clus3')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s =100, c = 'orange', label = 'clus4')
plt.title('clusters')
plt.show()