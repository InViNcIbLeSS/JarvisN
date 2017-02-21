import data
import nltk
import pickle
from nltk.tokenize import word_tokenize

class Brain:
	
	def __init__(self):
		self.train()
	
	def train(self):
		all_words_file = open("trainer/words.pickle", "rb")
		self.all_words = pickle.load(all_words_file)
		all_words_file.close()
		
		classifier_f = open("trainer/naivebayes.pickle", "rb")
		self.classifier = pickle.load(classifier_f)
		classifier_f.close()
		
	def getCommand(self, text):
		featurized_test_sentence = {i:(i in word_tokenize(text.lower())) for i in self.all_words}
		return self.classifier.classify(featurized_test_sentence)
	
	def getStats(self):
		print('stats', self.classifier.show_most_informative_features(10))