import sys
import config_data
sys.path.append(config_data.jarvis_folder_location)
from JarvisN.database.datahelper import DataDbHelper

td = []
dbh = DataDbHelper()
result = dbh.getResult("SELECT sentence, label2 FROM trainingdata WHERE label1='dictionary'")
dbh.closeConnection()

for row in result:
	td.append((row[0],row[1]))
print(td)