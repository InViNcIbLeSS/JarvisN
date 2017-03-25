import os
import sys
jarvis_folder_location=r"C:\Users\Dhaval\Documents\GitHub"			#Jarvis folder location
sys.path.append(jarvis_folder_location)
java_path = "C:\Program Files\Java\jdk1.8.0_101\\bin\java.exe"
os.environ['JAVAHOME'] = java_path

from jarvisClassifierN import JarvisClassifier
jc = JarvisClassifier()

while(True):
	print(jc.extractTag(input(),'dictionary','WORD'))