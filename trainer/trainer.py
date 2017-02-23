import data
import nltk
import pickle
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

import os
import sys
sys.path.append(r'C:\Users\Dhaval\Documents\GitHub')
from JarvisN.database.datahelper import DataDbHelper

td = data.training_data
ts = data.test_data