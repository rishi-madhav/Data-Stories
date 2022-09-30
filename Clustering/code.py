# --------------
# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.cluster import KMeans
from sklearn import preprocessing 
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


#Importing the mall dataset with pandas
dataset = pd.read_csv(path)
#print(dataset.head())


# Create an array
X = dataset.iloc[:, [3,4]].values
#print(X)

# Using the elbow method to find the optimal number of clusters
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
print(wcss)

# Plot the graph to visualize the Elbow Method to find the optimal number of cluster  
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# Applying KMeans to the dataset with the optimal number of cluster
kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
Y_KMeans = kmeans.fit_predict(X)


# Visualising the clusters
plt.scatter(X[Y_KMeans==0, 0], X[Y_KMeans==0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X[Y_KMeans==1, 0], X[Y_KMeans==1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X[Y_KMeans==2, 0], X[Y_KMeans==2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(X[Y_KMeans==3, 0], X[Y_KMeans==3, 1], s=100, c='cyan', label='Cluster 4')
plt.scatter(X[Y_KMeans==4, 0], X[Y_KMeans==4, 1], s=100, c='magenta', label='Cluster 5')

plt.title('Cluster of clients')
plt.xlabel('Annual Income')
plt.ylabel('Spending score')
plt.legend()
plt.show()

# Label encoding and plotting the dendogram
le = preprocessing.LabelEncoder()
dataset['Genre'] = le.fit_transform(dataset['Genre'])
dataset.drop(['CustomerID'], axis=1, inplace=True)
plt.figure(figsize = (10,7))
plt.title('Malls Customer Dendogram')

dend = sch.dendrogram(sch.linkage(dataset, method='ward'), leaf_rotation=90, leaf_font_size=2.4)
plt.show()



