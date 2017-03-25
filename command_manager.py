import os
from pygame import mixer
from gtts import gTTS
from modules.dictionary_module import Dictionary
import JarvisN.config_data as config_data
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger
import pyttsx
import random

class CommandManager:
	
	def __init__(self):
		self.engine = pyttsx.init('sapi5')
		self.diction = Dictionary()
		self.dictionary_tagger = StanfordNERTagger(config_data.directory_path+'\\tagger\\english.all.3class.distsim.crf.ser.gz',
						config_data.directory_path+'\\tagger\\stanford-ner.jar')
		self.tagger = {
			'dictionary':self.dictionary_tagger
			}
	
	def callCommand(self, text, msg):
		info = 'none'
		if text == 'greeting':
			self.greeting()
		elif text == 'music':
			self.music()
		elif text == 'question':
			self.question()
		elif text == 'dictionary':
			return self.dictionary(msg)
		else:
			self.speak('I do not understand')
		return info , info
			
	def greeting(self):
		response = ['hello sir', 'hi']
		
		self.speak(response[random.randint(0,1)])
		
	def music(self):
		self.speak('sorry sir, i can not play music now')
		
	def question(self):
		self.speak('sorry sir, i can not answer that question')
		
	def dictionary(self, word):
		info = self.extractTag(word, 'dictionary', 'WORD')
		meaning = self.diction.getMeaning(word)
		print(meaning)
		for k, v in meaning.items():
			z=v
		self.speak(z[0])
		print(info)
		return info , 'WORD'
		
	def speak(self,speech):
		self.engine.say(speech)
		self.engine.runAndWait()
		print('Spoke')
		
	def getTaggedSentence(self, sentence, tagger):
		tokenized_text = word_tokenize(sentence)
		classified_text = self.tagger[tagger].tag(tokenized_text)
		return classified_text
		
	def extractTag(self, sentence, tagger, tag):
		tagged_sentence = self.getTaggedSentence(sentence, tagger)
		for word in tagged_sentence:
			if(word[1] == tag):
				return word[0]