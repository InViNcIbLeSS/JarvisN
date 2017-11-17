import asyncio
import websockets
import os
import sys
import webbrowser
import config_data
sys.path.append(config_data.jarvis_folder_location)
from jarvisBrain import Brain
from classifier.jarvisClassifierN import JarvisClassifier
from command_manager import CommandManager
import pyttsx
from JarvisN.database.datahelper import DataDbHelper
engine = pyttsx.init('sapi5')

def speak(speech):
	engine.say(speech)
	engine.runAndWait()
	print('Spoke')

def main():
	
	os.chdir(config_data.directory_path)
	webbrowser.open('http://localhost/jarvis/jarvis.php')
	java_path = "C:\Program Files\Java\jdk1.8.0_101\\bin\java.exe"
	os.environ['JAVAHOME'] = config_data.java_path
	brain = Brain()
	classifier = JarvisClassifier()
	commandManager = CommandManager()
	db = DataDbHelper()
	
	async def hello(websocket, path):
	
		#Listen ----------
		print('started')
		msg = await websocket.recv()
		#msg = input('Enter command')
		print("< {}".format(msg))
		
		#cmd = brain.getCommand(msg)
		cmd = classifier.classify(msg,'general')
		if cmd == "greeting":
			sub = "NONE"
		else:
			sub = classifier.classify(msg,cmd)
		
		#React
		entity , type = commandManager.callCommand(cmd, sub, msg)
		print(cmd,sub,entity,type)
		if msg == " close" or msg == "close":
			asyncio.get_event_loop().stop()
		try:
			db.insertIntoNewData(msg, cmd, sub, 0,0,type)
		except:
			print("Entry exists")
		
	start_server = websockets.serve(hello, 'localhost', 9999)
	loop=asyncio.get_event_loop()#asyncio.get_event_loop().stop()
	loop.run_until_complete(start_server)
	loop.run_forever()

if __name__ == "__main__":
	main()