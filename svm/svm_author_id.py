#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# I made the trainig dataset smaller for the algorithm to be faster
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

# clf = SVC(kernel='linear') Best accuracy 0.9840728100113766 but it took a lot to train because I used the dataset completely
# SVM is slower than naive_bayes
# When the dataset is smaller, the accuracy is not high but the trainig time is much shorter
# When C increases, more points are taaken into account and the accuracy is higher
# With a high C, I end up with a more complex decision boundary


clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train,labels_train)
#accuracy = clf.score(features_test,labels_test)
print(clf.predict([features_test[50]]))


