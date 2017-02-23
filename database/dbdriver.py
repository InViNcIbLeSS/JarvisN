from datahelper import DataDbHelper
import data
td = data.training_data

dbh = DataDbHelper()
result = dbh.getTrainingDataCursor()
dbh.closeConnection()
