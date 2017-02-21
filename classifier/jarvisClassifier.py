import pickle
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize
from statistics import mode

class JarvisClassifier(ClassifierI):

	def __init__(self):
		all_words_file = open("classifier/words.pickle", "rb")
		self.all_words = pickle.load(all_words_file)
		all_words_file.close()
		classifier_f = open("classifier/general_classifiers.pickle", "rb")
		self.general_classifier = pickle.load(classifier_f)
		classifier_f.close()
		
	def classify(self, text):
		featurized_test_sentence = {i:(i in word_tokenize(text.lower())) for i in self.all_words}
		return self.getWinner(featurized_test_sentence)
		
	def test(self, text):
		featurized_test_sentence = {i:(i in word_tokenize(text.lower())) for i in self.all_words}
		print(self.getWinner(featurized_test_sentence), 'with', self.confidence(featurized_test_sentence))
		
	def getWinner(self, features):
		votes = []
		for c in self.general_classifier:
			v = c.classify(features)
			votes.append(v)
		return mode(votes)
		
	def confidence(self, features):
		votes = []
		for c in self.general_classifier:
			v = c.classify(features)
			votes.append(v)

		choice_votes = votes.count(mode(votes))
		conf = choice_votes / len(votes)
		return conf