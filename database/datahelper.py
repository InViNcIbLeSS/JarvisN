import MySQLdb

class DataDbHelper:
	
	def __init__(self):
		self.db = MySQLdb.connect("localhost","root","","jarvis" )
		self.cursor = self.db.cursor()
		
	def closeConnection(self):
		self.db.close()
	
	def insertIntoTrainingData(self,sent, label1, label2, es, ee, e):
		query = "INSERT INTO trainingdata(sentence, label1, label2, entitys, entitye, entity) \
				VALUES('%s', '%s', '%s', '%d', '%d', '%s')" % \
				(sent, label1, label2, es, ee, e)
		self.cursor.execute(query)
		
	def getTrainingDataCursor(self):
		query = "SELECT * FROM trainingdata"

		# Execute the SQL command
		self.cursor.execute(query)
		# Fetch all the rows in a list of lists.
		results = self.cursor.fetchall()
		return results
		
	def getResult(self, query):
		# Execute the SQL command
		self.cursor.execute(query)
		# Fetch all the rows in a list of lists.
		results = self.cursor.fetchall()
		return results
		