import pickle

class JarvisClassifier:

	def __init__(self):
		classifier_f = open("naivebayes.pickle", "rb")
		self.nbclassifier = pickle.load(classifier_f)
		classifier_f = open("naivebayes.pickle", "rb")
		self.nbclassifier = pickle.load(classifier_f)
		classifier_f = open("naivebayes.pickle", "rb")
		self.nbclassifier = pickle.load(classifier_f)
		classifier_f = open("naivebayes.pickle", "rb")
		self.nbclassifier = pickle.load(classifier_f)
		classifier_f = open("naivebayes.pickle", "rb")
		self.nbclassifier = pickle.load(classifier_f)
		classifier_f = open("naivebayes.pickle", "rb")
		self.nbclassifier = pickle.load(classifier_f)
		classifier_f.close()
		
	def classify(self):
		