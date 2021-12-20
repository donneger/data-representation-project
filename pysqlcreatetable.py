# program to create the gym bookings table in the datarepresentation schema. 
import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="datarepresentation",
auth_plugin='mysql_native_password'
)


cursor = db.cursor()

sql="CREATE TABLE gymbooking (id INT AUTO_INCREMENT PRIMARY KEY, membername VARCHAR(255), age int, class varchar(255), classdate varchar(255), classtime varchar(255), instructor varchar(255))"

cursor.execute(sql)

db.commit()

print("Gym Booking Table created in db")