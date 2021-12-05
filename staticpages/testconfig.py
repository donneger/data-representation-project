import mysql.connector
import dbconfig as cfg


bookdb = mysql.connector.connect(
host = cfg.mysql['host'],
user = cfg.mysql['user'],
password = cfg.mysql['password'],
database = cfg.mysql['database']
        )

cursor=bookdb.cursor()

sql = "select * from books"

cursor.execute(sql)

result = cursor.fetchall()

for x in result:

    print(x)
