import pickle
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger
from statistics import mode
from JarvisN import config_data

class JarvisClassifier(ClassifierI):

	def __init__(self):
		all_words_file = open(config_data.directory_path+"\classifier\words.pickle", "rb")
		self.all_words = pickle.load(all_words_file)
		all_words_file.close()
		classifier_f = open(config_data.directory_path+"\classifier\general_classifiers.pickle", "rb")
		self.general_classifier = pickle.load(classifier_f)
		classifier_f = open(config_data.directory_path+"\classifier\dictionary_classifiers.pickle", "rb")
		self.dictionary_classifier = pickle.load(classifier_f)
		classifier_f = open(config_data.directory_path+"\classifier\music_classifiers.pickle", "rb")
		self.music_classifier = pickle.load(classifier_f)
		classifier_f.close()
		
		self.dictionary_tagger = StanfordNERTagger(config_data.directory_path+'\\tagger\\english.all.3class.distsim.crf.ser.gz',
						config_data.directory_path+'\\tagger\\stanford-ner.jar')
		
		self.classifier_type = {
			'general':self.general_classifier,
			'dictionary':self.dictionary_classifier,
			'question':self.general_classifier,
			'music':self.music_classifier
			}
		self.tagger = {
			'dictionary':self.dictionary_tagger
			}
		
	def classify(self, text, classifier_name):
		
		featurized_test_sentence = {i:(i in word_tokenize(text.lower())) for i in self.all_words}
		return self.getWinner(featurized_test_sentence, self.classifier_type[classifier_name])
		
	def test(self, text):
		featurized_test_sentence = {i:(i in word_tokenize(text.lower())) for i in self.all_words}
		print(self.getWinner(featurized_test_sentence), 'with', self.confidence(featurized_test_sentence))
		
	def getWinner(self, features, classifiers):
		votes = []
		for c in classifiers:
			v = c.classify(features)
			votes.append(v)
		return mode(votes)
		
	def confidence(self, features, classifiers):
		votes = []
		for c in classifiers:
			v = c.classify(features)
			votes.append(v)

		choice_votes = votes.count(mode(votes))
		conf = choice_votes / len(votes)
		return conf
		
	def getTaggedSentence(self, sentence, tagger):
		tokenized_text = word_tokenize(sentence)
		classified_text = self.tagger[tagger].tag(tokenized_text)
		return classified_text
		
	def extractTag(self, sentence, tagger, tag):
		tagged_sentence = self.getTaggedSentence(sentence, tagger)
		for word in tagged_sentence:
			if(word[1] == tag):
				return word[0]