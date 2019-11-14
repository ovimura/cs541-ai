# from math import sqrt
#
# row1 = [5.1,3.5,1.4,0.2,'Iris-setosa']
# row2 = [4.9,3.0,1.4,0.2,'Iris-setosa']
# row3 = [4.7,3.2,1.3,0.2,'Iris-setosa']
# row4 = [4.6,3.1,1.5,0.2,'Iris-setosa']
# row5 = [5.0,3.6,1.4,0.2,'Iris-setosa']
#
#
# # calculate the Euclidean distance between two vectors
# def euclidean_distance(row1, row2):
# 	distance = 0.0
# 	for i in range(len(row1)-1):
# 		distance += (row1[i] - row2[i])**2
# 	return sqrt(distance)
#
# print(euclidean_distance(row1, row2))



import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set()



breast_cancer = load_breast_cancer()
X = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
X = X[['mean area', 'mean compactness']]
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)
y = pd.get_dummies(y, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

sns.scatterplot(
    x='mean area',
    y='mean compactness',
    hue='benign',
    data=X_test.join(y_test, how='outer')
)

confusion_matrix(y_test, y_pred)
