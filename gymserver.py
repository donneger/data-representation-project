from flask import Flask, url_for, request, redirect, abort, jsonify
from gymDAO import gymDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


nextid=5
#Home Page
@app.route('/')
def index():
    return "hello world"

# Get all Data
@app.route('/books')
def getAll():
    return jsonify(gymDao.getAll())

# Get a specific record
@app.route('/books/<int:ISBN>')
def findById(ISBN):
    return jsonify(gymDao.findById(ISBN))


# Add a new record
@app.route('/books', methods = ['POST'])
def create():
    if not request.json:
        abort(400)
    book = {
    "ISBN": request.json['ISBN'], 
    "title": request.json["title"], 
    "author": request.json["author"],
    "price": request.json["price"]
    }
    return jsonify(gymDao.create(book))

# Update a record
@app.route('/books/<int:ISBN>', methods = ['PUT'])
def update(ISBN):
    foundBook = gymDao.findById(ISBN)
    print(foundBook)
    if len(foundBook) == 0:
        return jsonify({}), 404      
    currentBook = foundBook
    if 'title' in request.json:
        currentBook['title'] = request.json['title']
    if 'author' in request.json:
        currentBook['author'] = request.json['author']
    if 'price' in request.json:
            currentBook['price'] = request.json['price']
    gymDao.update(currentBook)

    return jsonify(currentBook)

# Delete a record
@app.route('/books/<int:ISBN>', methods = ['DELETE'])
def delete(ISBN):
    foundBook = gymDao.findById(ISBN)
    print(foundBook)
    if len(foundBook) == 0:
        return jsonify({}), 404
    gymDao.delete(ISBN)
    return jsonify({"done":True})


if __name__ == "__main__":
    print("in if")
    app.run(debug=True)