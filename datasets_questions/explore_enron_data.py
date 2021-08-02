#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
number_of_people = len(enron_data)
print(number_of_people) # Output: 146
number_of_features = len(enron_data['METTS MARK'])
print(number_of_features) # Output: 21


# Number of persons of interest in enron dataset
number_of_persons_of_interests = 0
for person_features in enron_data.values():
    if person_features['poi'] == 1:
        number_of_persons_of_interests += 1
print(number_of_persons_of_interests) # Output: 18


# Total number of persons of interest
poi_total = 0
with open('../final_project/poi_names.txt', 'r') as file:
    text = file.read()
    lines = text.split('\n')
    poi_total = len(lines) - 3
print(poi_total) # Output: 35

# Total value of the stock belonging to James Prentice
print(enron_data['PRENTICE JAMES']['total_stock_value']) # Output: 1095040

# Number of email messages from Wesley Colwell to persons of interest
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi']) # Output: 11

# Value of stock options exercised by Jeffrey K Skilling
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options']) # Output: 19250000

# How much money Ken Lay took home
print(enron_data['LAY KENNETH L']['total_payments']) #Output: 103559793

# How many folks in this dataset have a quantified salary? What about a known email address?
counter = 0
for person,information in enron_data.items():
    if information['salary'] != 'NaN':
        counter += 1
print(counter) # Output: 95

counter = 0
for person,information in enron_data.items():
    if information['email_address'] != 'NaN':
        counter += 1
print(counter)# Output: 111


# What percentage of people in the dataset have "NaN" for their total payments?
people_total = 0
existing_total_payments = 0
for person,information in enron_data.items():
    people_total += 1
    if information['total_payments'] != 'NaN':
        existing_total_payments += 1


print(existing_total_payments) # Output: 125
print(people_total) # Output: 146
print(1 - float(existing_total_payments)/people_total) # 0.14

# Number of persons of interest in enron dataset with 'NaN' for total_payments
poi_missing_total_payments = 0
for person_features in enron_data.values():
    if person_features['poi'] == 1 and person_features['total_payments'] == 'NaN':
        poi_missing_total_payments += 1
print(poi_missing_total_payments / float(number_of_persons_of_interests)) # Output: 0