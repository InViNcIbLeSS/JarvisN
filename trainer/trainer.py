import data
import nltk
import pickle
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

td = data.training_data
ts = data.test_data
all_words = set(word.lower() for passage in td for word in word_tokenize(passage[0]))
training_set = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in td]
testing_set = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in ts]
classifier = nltk.NaiveBayesClassifier.train(training_set)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MultinomialNB accuracy percent:",nltk.classify.accuracy(MNB_classifier, training_set))

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BernoulliNB accuracy percent:",nltk.classify.accuracy(BNB_classifier, training_set))

print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

#NuSVC_classifier = SklearnClassifier(NuSVC())
#NuSVC_classifier.train(training_set)
#print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier = open("mnnaivebayes.pickle","wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier = open("bnaivebayes.pickle","wb")
pickle.dump(BNB_classifier, save_classifier)
save_classifier = open("logisticRegression.pickle","wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier = open("SGDClassifier.pickle","wb")
pickle.dump(SGDClassifier_classifier, save_classifier)
save_classifier = open("SVCclassifier.pickle","wb")
pickle.dump(SVC_classifier, save_classifier)
save_classifier = open("linearSVCclassifier.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

f = open("words.pickle","wb")
pickle.dump(all_words, f)
f.close()



print('stats', classifier.show_most_informative_features(10))