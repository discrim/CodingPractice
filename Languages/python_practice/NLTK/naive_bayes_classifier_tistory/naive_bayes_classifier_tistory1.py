import nltk
from nltk.corpus import movie_reviews
import pandas as pd
import pickle
 
# https://www.pythonprogramming.net/naive-bayes-classifier-nltk-tutorial/
 
# =======================================
# -- Get dataset from dump
# =======================================
# Ref : dbrang.tistory.com/1239
 
featuresets = []
 
with open ('featuresets.dmp', 'rb') as fp:
    featuresets = pickle.load(fp)
 
print(featuresets[0])
print("... features_sets", "." * 100, "\n")
 
print(len(featuresets))
print("... len(featuresets)", "." * 100, "\n")
 
 
# =======================================
# -- Naive Bayes Classifier
# =======================================
 
# -- set training data
training_set = featuresets[:1900]
 
# -- set test data
testing_set = featuresets[1900:]
 
# -- define classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)
 
# -- get accuracy
print((nltk.classify.accuracy(classifier, testing_set))*100, '%')
print(",,, Classifier accuracy percent", "," * 100, "\n")
 
classifier.show_most_informative_features(50)
print(",,, show_most_informative_features", "," * 100, "\n")
 
 
# =======================================
# -- Save and load Classifiers with NLTK
# =======================================
 
# -- Save classifier with pickle
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
 
# -- Load classifier from pickle
classifier_f = open("naivebayes.pickle", "rb")
classifier_new = pickle.load(classifier_f)
classifier_f.close()
 
print(type(classifier_new))
print(";;; Classifier type", ";" * 100, "\n")
 
# -- Reuse classifier
print((nltk.classify.accuracy(classifier_new, featuresets))*100, '%')
print(";;; New Classifier accuracy percent", ";" * 100, "\n")