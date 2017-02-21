from PyDictionary import PyDictionary
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger

class Dictionary:
	
	def __init__(self):
		self.dictionary=PyDictionary()
		self.st = StanfordNERTagger('D:\Python\stanford-ner-2016-10-31\classifiers\english.all.3class.distsim.crf.ser.gz',
						'D:\Python\stanford-ner-2016-10-31\stanford-ner.jar')
		
	def getMeaning(self, word):
		tokenized_text = word_tokenize(word)
		classified_text = self.st.tag(tokenized_text)

		print(classified_text)

		for i in classified_text:
			if(i[1] == 'WORD'):
				return self.dictionary.meaning(i[0])