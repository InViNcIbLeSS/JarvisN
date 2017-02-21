import asyncio
import websockets
import os
from pygame import mixer
from gtts import gTTS
from tempfile import TemporaryFile
import sys
import webbrowser
from jarvisBrain import Brain
from command_manager import CommandManager
import pyttsx
engine = pyttsx.init('sapi5')

def speak(speech):
	engine.say(speech)
	engine.runAndWait()
	print('Spoke')

def main():
	
	os.chdir('D:Python/Jarvis-master')
	#webbrowser.open('http://localhost/jarvis/jarvis.php')
	java_path = "C:\Program Files\Java\jdk1.8.0_101\\bin\java.exe"
	os.environ['JAVAHOME'] = java_path
	brain = Brain()
	commandManager = CommandManager()
	
	while(True):
	
		msg = input()
		cmd = brain.getCommand(msg)
		#React
		commandManager.callCommand(cmd, msg)
		if msg == " close" or msg == "close":
			break
	print("closed")
			
		
		
	

if __name__ == "__main__":
	main()