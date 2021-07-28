#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import numpy
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

"""
# Using a linear kernel and the whole dataset
# accuracy == 0.98

clf = SVC(kernel='linear')
clf.fit(features_train,labels_train)
accuracy = clf.score(features_test,labels_test)
print(accuracy)
"""

"""
# Using a linear kernel and a smaller dataset
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
# Accuracy == 0.88

clf = SVC(kernel='linear')
clf.fit(features_train,labels_train)
accuracy = clf.score(features_test,labels_test)
print(accuracy)
"""

"""
# Using a rbf kernel and a smaller dataset
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
# Accuracy == 0.61

clf = SVC(kernel='rbf')
clf.fit(features_train,labels_train)
accuracy = clf.score(features_test,labels_test)
print(accuracy)
"""

"""
# Using a rbf kernel, a smaller dataset, and C equals 10000
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
# Accuracy == 0.89

clf = SVC(kernel='rbf')
clf.fit(features_train,labels_train)
accuracy = clf.score(features_test,labels_test)
print(accuracy)
"""

"""
# Using a rbf kernel, the whole dataset, and C equals 10000
# Accuracy == 0.99

clf = SVC(kernel='rbf')
clf.fit(features_train,labels_train)
accuracy = clf.score(features_test,labels_test)
print(accuracy)
"""

"""
# Reducing the dataset size and predicting the author of some emails
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train,labels_train)
email1 = features_test[10]
email2 = features_test[26]
email3 = features_test[50]
prediction = clf.predict([email1,email2,email3])
print(prediction)
"""

# Using the whole dataset and identifying Chris' emails
# {0: 881, 1: 877}

clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train,labels_train)
prediction = clf.predict(features_test)
unique, counts = numpy.unique(prediction, return_counts=True)
print(dict(zip(unique, counts)))
