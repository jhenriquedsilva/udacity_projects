#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset

        path = os.path.join('..', path[:-1])
        email = open(path, "r")

        ### use parseOutText to extract the text from the opened email
        stemmed_email = parseOutText(email)
        print "OLD EMAIL"
        print stemmed_email
        print "\n"
        ### use str.replace() to remove any instances of the words
        ### ["sara", "shackleton", "chris", "germani"]
        stemmed_email = stemmed_email.replace('sara','').replace('shackleton','').replace('chris','').replace('germani','')
        print "NEM EMAIL"
        print stemmed_email

        ### append the text to word_data
        word_data.append(stemmed_email)
        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
        if name == "sara":
            from_data.append(0)
        else:
            from_data.append(1)

        email.close()

print "POSITION 152"        
print word_data[152]
print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )



"""
In sklearn, Bag of Words is called CountVectorizer. Actually, it creates a bag of words
from sklearn.feature_extraction.text import CountVectorizer
string1 = "hi my name"
string2 = "select that job"
string3 = "I am really good at crazy"
emails = [string1, string2, string3]
vectorizer = CountVectorizer()
bag_of_words = vectorizer.fit_transform(emails) # Assigns numbers to each word and counts them
vectorizer.vocabulary_.get("job") -> How to get the nunber of a word
(0, 7)        1 -> In document number 0, word 7 occurs 1 time

from nltk.corpus import stopwords
sw = stopwords.words('english')

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
stemmer.stem('responsiveness')

Tfidf represation -> Term frequency inverse document frequency
weighting by how often a word occurs in all the documments put together
"""
### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text

stopwords = list(text.ENGLISH_STOP_WORDS)
print "THIS ARE THE STOPWORDS"
print stopwords
vectorizer = TfidfVectorizer(stop_words=stopwords)
bag_of_words = vectorizer.fit_transform(word_data)
print "THIS IS THE MATRIX:"
print bag_of_words
print "MAPPING:"
# I think I have to set this
mapping = set(vectorizer.get_feature_names())
print mapping
print "NUMBER OF WORDS:"
print len(mapping)