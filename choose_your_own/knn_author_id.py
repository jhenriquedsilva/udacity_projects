#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.neighbors import KNeighborsClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################

"""
# I chose KNN in this exploratory exercise
# Using n_neighbors equals 5
# Accuracy 0.92
clf = KNeighborsClassifier()
clf.fit(features_train, labels_train)
accuracy = clf.score(features_test, labels_test)
print(accuracy)
"""
# n_neighbors equals 1 (default==5), but I think it is overfitting
# Accuracy 0.94
clf = KNeighborsClassifier(n_neighbors=1)
clf.fit(features_train, labels_train)
accuracy = clf.score(features_test, labels_test)
print(accuracy)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
