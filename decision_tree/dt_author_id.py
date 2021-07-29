#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

"""
# First using a decision tree with min_samples_split equals 40 and 10% of all features
# Accuracy equals 0.978
clf = DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train,labels_train)
accuracy = clf.score(features_test,labels_test)
print(accuracy)
"""

"""
# The more features an algorithm deals with, the more time is necessary to train it
# A large value for percentile lead to a more complex decision tree
# Here percentile is equal to 10 in email_preprocess.py file, and the number of features is 3785
# selector = SelectPercentile(f_classif, percentile=1)
print(len(features_train[0]))
"""

"""
# After changind the percentile to 1 in email_preprocess.py file, the new number of features is 379
# selector = SelectPercentile(f_classif, percentile=1)
print(len(features_train[0]))
"""

# Accuracy using a decision tree with min_samples_split equals 40 and 1% of all features
# Accuracy equals 0.966
clf = DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train,labels_train)
accuracy = clf.score(features_test,labels_test)
print(accuracy)