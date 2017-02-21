from datahelper import DataDbHelper
import data
td = data.training_data

dbh = DataDbHelper()
dbh.getTrainingDataCursor()
dbh.closeConnection()
