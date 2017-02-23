import asyncio
import websockets
import os
import sys
import webbrowser
import config_data
from jarvisBrain import Brain
from classifier.jarvisClassifier import JarvisClassifier
from command_manager import CommandManager
import pyttsx
engine = pyttsx.init('sapi5')

def speak(speech):
	engine.say(speech)
	engine.runAndWait()
	print('Spoke')

def main():
	
	sys.path.append(config_data.directory_path)
	os.chdir(config_data.directory_path)
	#webbrowser.open('http://localhost/jarvis/jarvis.php')
	java_path = "C:\Program Files\Java\jdk1.8.0_101\\bin\java.exe"
	os.environ['JAVAHOME'] = config_data.java_path
	brain = Brain()
	classifier = JarvisClassifier()
	commandManager = CommandManager()
	
	while(True):
	
		msg = input()
		#cmd = brain.getCommand(msg)
		cmd = classifier.classify(msg)
		#React
		commandManager.callCommand(cmd, msg)
		if msg == " close" or msg == "close":
			break
	print("closed")
			
		
		
	

if __name__ == "__main__":
	main()