# Progarm to create the database for the Gym Booking Schema. 
# Author: Gerry Donnelly, Dec 2021
import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
password="root",
auth_plugin='mysql_native_password'
)


cursor = db.cursor()

# Creating the database schema called datarepresentation.
cursor.execute("CREATE DATABASE datarepresentation")

print("datarepresentation schema created")