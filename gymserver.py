from flask import Flask, url_for, request, redirect, abort, jsonify
from gymDAO import gymDao
from datetime import date, datetime

app = Flask(__name__, static_url_path='', static_folder='staticpages')


nextid=5
#Home Page
@app.route('/')
def index():
    return "hello world"

# Get all Data
@app.route('/gymbooking')
def getAll():
    return jsonify(gymDao.getAll())

# Get a specific record
@app.route('/gymbooking/<int:id>')
def findById(ISBN):
    return jsonify(gymDao.findById(id))


# Add a new record
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

# Update a record
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

# Delete a record
@app.route('/gymbooking/<int:id>', methods = ['DELETE'])
def delete(id):
    foundBooking = gymDao.findById(id)
    print(foundBooking)
    if len(foundBooking) == 0:
        return jsonify({}), 404
    gymDao.delete(id)
    return jsonify({"done":True})


if __name__ == "__main__":
    print("in if")
    app.run(debug=True)