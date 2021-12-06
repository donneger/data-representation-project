import mysql.connector
from mysql.connector import cursor

class GymDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'datarepresentation'
        )

        #print('connection made')

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

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from gymbooking'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print('results from getall are',results)
        for result in results:
            resultAsDict=self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

    
    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from gymbooking where id = %s'
        values=[id]
        cursor.execute(sql, values)
        result=cursor.fetchone()
        #print('results from findby are',result)
        return self.convertToDict(result)


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

    def delete(self, id):
        cursor = self.db.cursor()
        sql = 'delete from gymbooking where id = %s'
        values=[id]
        cursor.execute(sql, values)
        self.db.commit()
        print('delete complete')
        return {}


    def convertToDict(self, result):
        colnames = ['id','membername', 'age', 'class', 'classdate', 'classtime', 'instructor' ]
        booking = {}
        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                booking[colName] = value
            return booking

gymDao = GymDAO()