# Program for running server for Gym Booking System.
# Author: Gerry Donnelly Dec 2021

# Import the relevant modules.
from flask import Flask, url_for, request, redirect, abort, jsonify
from gymDAO import gymDao
from datetime import date, datetime

app = Flask(__name__, static_url_path='', static_folder='staticpages')


#Home Page
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Get all the Data from the bookings database.
@app.route('/gymbooking')
def getAll():
    return jsonify(gymDao.getAll())

# Get a specific booking from the database.
@app.route('/gymbooking/<int:id>')
def findById(ISBN):
    return jsonify(gymDao.findById(id))


# Add a new booking to the database.
@app.route('/gymbooking', methods = ['POST'])
def create():
    if not request.json:
        abort(400)
    booking = {
    "membername": request.json['membername'], 
    "age": request.json["age"], 
    "class": request.json["class"],
    "classdate": request.json["classdate"],
    "classtime": request.json["classtime"],
    "instructor": request.json["instructor"]
    }
    return jsonify(gymDao.create(booking))

# Update an existing gym booking record.
@app.route('/gymbooking/<int:id>', methods = ['PUT'])
def update(id):
    foundBooking = gymDao.findById(id)
    print(foundBooking)
    if len(foundBooking) == 0:
        return jsonify({}), 404      
    currentBooking = foundBooking
    if 'membername' in request.json:
        currentBooking['membername'] = request.json['membername']
    if 'age' in request.json:
        currentBooking['age'] = request.json['age']
    if 'class' in request.json:
            currentBooking['class'] = request.json['class']
    if 'classdate' in request.json:
            currentBooking['classdate'] = request.json['classdate']
    if 'classtime' in request.json:
        currentBooking['classtime'] = request.json['classtime']
    if 'instructor' in request.json:
            currentBooking['instructor'] = request.json['instructor']
    gymDao.update(currentBooking)
    return jsonify(currentBooking)

# Delete a gym booking record.
@app.route('/gymbooking/<int:id>', methods = ['DELETE'])
def delete(id):
    foundBooking = gymDao.findById(id)
    print(foundBooking)
    if len(foundBooking) == 0:
        return jsonify({}), 404
    gymDao.delete(id)
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)