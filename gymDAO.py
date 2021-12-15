# Data Access Object (DOA) for the Gym Booking Website
# Author: Gerry Donnelly December

import mysql.connector
from mysql.connector import cursor

# Setting up the database class that will be called from the gymserver program. 
class GymDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'datarepresentation'
        )

# Function to create a new booking into the database called from the flask server. 
# Data is entered on the web page and returned from the server function and written to the database. 
    def create(self,booking):
        cursor = self.db.cursor()
        sql = "insert into gymbooking (membername, age, class, classdate, classtime, instructor) values(%s,%s,%s,%s,%s,%s)"
        values = [
            booking['membername'],
            booking['age'],
            booking['class'],
            booking['classdate'],
            booking['classtime'],
            booking['instructor']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

# Function to return all of the records from the database, the array returned is provided to the server for writing to the web page. 
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from gymbooking'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict=self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

# Function to find a specifc record, used when the booking update is selected on the web page, the data is returned to the webpage and displaed in the update form.
    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from gymbooking where id = %s'
        values=[id]
        cursor.execute(sql, values)
        result=cursor.fetchone()
        #print('results from findby are',result)
        return self.convertToDict(result)

# Function to update a specific booking record. The findById function returns the record to be updated and this function takes the updates and writes back to the database. 
    def update(self,booking):
        cursor = self.db.cursor()
        sql = "update gymbooking set membername = %s, age = %s, class = %s, classdate=%s, classtime=%s, instructor=%s where id = %s"
        values = [
            booking['membername'],
            booking['age'],
            booking['class'],
            booking['classdate'],
            booking['classtime'],
            booking['instructor'],
            booking['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return booking

# Function to delete a specific record from the database.
    def delete(self, id):
        cursor = self.db.cursor()
        sql = 'delete from gymbooking where id = %s'
        values=[id]
        cursor.execute(sql, values)
        self.db.commit()
        print('delete complete')
        return {}

# Function to convert the records from the database to a dict type that can be written to the web page. 
    def convertToDict(self, result):
        colnames = ['id','membername', 'age', 'class', 'classdate', 'classtime', 'instructor' ]
        booking = {}
        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                booking[colName] = value
            return booking

gymDao = GymDAO()