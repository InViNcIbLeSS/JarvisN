import asyncio
import websockets
import os
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
	
	os.chdir('D:Python/Jarvis')
	webbrowser.open('http://localhost/jarvis/jarvis.php')
	java_path = "C:\Program Files\Java\jdk1.8.0_101\\bin\java.exe"
	os.environ['JAVAHOME'] = java_path
	brain = Brain()
	commandManager = CommandManager()
	
	async def hello(websocket, path):
	
		#Listen ----------
		msg = await websocket.recv()
		#msg = input('Enter command')
		print("< {}".format(msg))
		
		# THINK HERE ----------------------------------------------
		#------
		#------
		cmd = brain.getCommand(msg)
		
		#React
		commandManager.callCommand(cmd, msg)
		if msg == " close" or msg == "close":
			asyncio.get_event_loop().stop()
			
		#Reply
		#speak(msg)
		
	start_server = websockets.serve(hello, 'localhost', 9999)
	loop=asyncio.get_event_loop()
	loop.run_until_complete(start_server)
	loop.run_forever()

if __name__ == "__main__":
	main()