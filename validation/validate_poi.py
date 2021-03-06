#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list,sort_keys = '../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)
features_train,features_test,labels_train, labels_test = train_test_split(features,labels,random_state=42,test_size=0.3)


### it's all yours from here forward!  
clf = DecisionTreeClassifier()
# print labels_test
# print float((len(labels_test) - 4)) / len(labels_test)
clf.fit(features_train,labels_train)
print clf.predict(features_test)
accuracy = clf.score(features_test, labels_test)
print accuracy
print "Precision score: ", precision_score(labels_test, clf.predict(features_test))
print "Recall score: ", recall_score(labels_test, clf.predict(features_test))
