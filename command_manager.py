import os
from pygame import mixer
from gtts import gTTS
from modules.dictionary_module import Dictionary
import pyttsx
import random

class CommandManager:
	
	def __init__(self):
		self.engine = pyttsx.init('sapi5')
		self.diction = Dictionary()
	
	def callCommand(self, text, msg):
		if text == 'greeting':
			self.greeting()
		elif text == 'music':
			self.music()
		elif text == 'question':
			self.question()
		elif text == 'dictionary':
			self.dictionary(msg)
		else:
			self.speak('I do not understand')
			
	def greeting(self):
		response = ['hello sir', 'hi']
		
		self.speak(response[random.randint(0,1)])
		
	def music(self):
		self.speak('sorry sir, i can not play music now')
		
	def question(self):
		self.speak('sorry sir, i can not answer that question')
		
	def dictionary(self, word):
		meaning = self.diction.getMeaning(word)
		print(meaning)
		for k, v in meaning.items():
			z=v
		self.speak(z[0])
		
	def speak(self,speech):
		self.engine.say(speech)
		self.engine.runAndWait()
		print('Spoke')