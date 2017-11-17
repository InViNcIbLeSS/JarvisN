import data
import nltk
import pickle
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
import sys
import os
sys.path.append(r"C:\Users\Dhaval\Documents\GitHub")                   # Your JarvisN folder Location... Replace it
from JarvisN.database.datahelper import DataDbHelper				   # Rename folder to JarvisN not JarvisN-Master

#td = []
dbh = DataDbHelper()
#result = dbh.getResult("SELECT sentence, label1 FROM trainingdata")	   # execute ur query here
result = dbh.getResult("SELECT sentence, entitys, entitye, entity FROM trainingdata WHERE label1='music'")	   # execute ur query here
dbh.closeConnection()
file = open('nerData.tsv','w')
for row in result:
	sentence = row[0].split(" ")
	start = row[1]
	end = row[2]
	if row[3] == 'none':
		continue
	print(start,end)
	i = 0
	for word in sentence:
		if i >= start and i<end:
			file.write(word + "\t" + row[3])
		else:
			file.write(word + "\t" + "O")
		file.write("\n")
		i = i + 1
	file.write("." + "\t" + "O\n")
	#print(row[0],row[1])
file.close()
os.system("java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop austen.prop")