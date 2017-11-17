import os
import sys
import webbrowser
import JarvisN.config_data
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger
from itertools import groupby
from JarvisN.database.datahelper import DataDbHelper

class Music:
	
	def __init__(self):
		self.st = StanfordNERTagger(JarvisN.config_data.directory_path + '\\tagger\\ner-song-model.ser.gz',
						JarvisN.config_data.directory_path+'\\tagger\\stanford-ner.jar')
		self.db = DataDbHelper()
	def tag(self, sent):
		tokenized_text = word_tokenize(sent)
		classified_text = self.st.tag(tokenized_text)
		print(classified_text)
		entity, value = self.chunk(classified_text)
		return entity, value
		#for tag, chunk in groupby(classified_text, lambda x:x[1]):
		#	if tag != "O":
		#		print("%-12s"%tag, " ".join(w for w, t in chunk))
	def chunk(self, tagged_sent):
		for tag, chunk in groupby(tagged_sent, lambda x:x[1]):
			if tag != "O":
				first = tag
				sec = " ".join(w for w, t in chunk)
				#print("%-12s"%tag, " ".join(w for w, t in chunk))
				return first, sec
	def playSong(self, name):
		songResult = self.db.getSong(name)
		location = songResult[0][1]
		print(location)
		webbrowser.open(location)
		
	def playRandSong(self):
		print("in rand song")
		songResult = self.db.getRandomSong()
		location = songResult[1]
		print(location)
		webbrowser.open(location)