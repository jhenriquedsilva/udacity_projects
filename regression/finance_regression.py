#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    


import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.
from sklearn.linear_model import LinearRegression


# I used bonus against salary here and the result is really bad
reg = LinearRegression()
reg.fit(feature_train, target_train)
print "The slope is",reg.coef_ # Output: 5.44
print "The intercept is",reg.intercept_ # Output: -102360.54
# R squared on training data
print "R squared on training data is",reg.score(feature_train,target_train) # Output: 0.04550919269952436
# R squared on test data
print "R squared on test data is",reg.score(feature_test,target_test) # Output: -1.48499241736851


"""
# I used bonus against long_term_incentive here and the result is still bad
reg = LinearRegression()
reg.fit(feature_train, target_train)
print "The slope is",reg.coef_ # Output: 1.19
print "The intercept is",reg.intercept_ # Output: 554478.7562150093
# R squared on training data
print "R squared on training data is",reg.score(feature_train,target_train) # Output: 0.21708597125777662
# R squared on test data
print "R squared on test data is",reg.score(feature_test,target_test) # Output: -0.5927128999498639
"""

### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass

reg.fit(feature_test, target_test)
print "The slope is",reg.coef_ 
print "The intercept is",reg.intercept_
print "R squared on test data is",reg.score(feature_train,target_train)

plt.plot(feature_train, reg.predict(feature_train), color="b")


plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
