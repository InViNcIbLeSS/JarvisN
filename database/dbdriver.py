from datahelper import DataDbHelper

dbh = DataDbHelper()
print(dbh.getRandomSong())
dbh.closeConnection()
