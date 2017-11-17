import os
import sys
jarvis_folder_location=r"C:\Users\Dhaval\Documents\GitHub"			#Jarvis folder location
sys.path.append(jarvis_folder_location)
java_path = "C:\Program Files\Java\jdk1.8.0_101\\bin\java.exe"
os.environ['JAVAHOME'] = java_path

from music_module import Music
import JarvisN.config_data

m = Music()
ent, name = m.tag('play sky full of stars')
m.playSong(name)