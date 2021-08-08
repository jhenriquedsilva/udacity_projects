#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL', None)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
# IDENTIFYING OUTLIERS


# Identifying who has the highest salary
highest = 0
print type(highest)
for name,features in data_dict.items():
    if (type(features['salary']) == int) and (features['salary'] > highest):
        print name
        highest = features['salary']

print 

#Identifying who has the highest bonus
highest_bonus = 0
for name,features in data_dict.items():
    if (type(features['bonus']) == int) and (features['bonus'] > highest_bonus):
        print name
        highest_bonus = features['bonus']


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()