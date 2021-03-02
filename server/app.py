from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
from datetime import datetime
import mysql.connector
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

class Book:

    def __init__(self):
        self.title = ''
        self.author = []
        self.cover = ''
        self.read = ''
        self.reading = ''

    def __init__(self, read, reading):
        self.title = ''
        self.author = []
        self.cover = ''
        self.read = read
        self.reading = reading

    def toJson(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    def print(self):
        print("Title: " + str(self.title) +
              "\nAuthor: " + str(self.author) +
              "\nRead: " + str(self.read) +
              "\nReading: " + str(self.reading) +
              "\nCover: " + str(self.cover))

POSTS = [
    {
        'id': uuid.uuid4().hex,
        'timestamp': datetime.now(),
        'message': 'Hello World',
    }
]

HOST = 'book-site-first-db.cmib8iu7awys.us-east-2.rds.amazonaws.com'
USER = 'devinBooker'
PASSWD = 'poopy69Devco'
DATABASE = 'book_db_69'

@app.route('/books', methods=['POST'])
def all_books():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    BOOKS.append({
        'id': uuid.uuid4().hex,
        'title': post_data.get('title'),
        'author': post_data.get('author'),
        'read': post_data.get('read'),
        'reading': post_data.get('reading'),
    })
    response_object['message'] = 'Book added!'

@app.route('/books/<reader_id>', methods=['GET'])
def user_books(reader_id):
    response_object = {'status': 'success'}
    books = []
    book_objects = []
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        database=DATABASE
    )
    cursor = conn.cursor()

    # Get ID for books attached to the reader
    # Response ex. (1,1,1), (2,0,1), (book id, read, reading)
    cursor.execute('SELECT book_id,red,reading FROM readers_books WHERE reader_id=' + str(reader_id))
    for row in cursor:
        books.append(row)
    
    # For each book id recieved, get details
    for book in books:
        auth_id = []
        book_key = book[0]
        book_object = Book(book[1], book[2])

        # Look up book in books table
        cursor.execute('SELECT title,cover FROM books WHERE id=' + str(book_key))
        for (title, cover) in cursor:
            book_object.title = title
            book_object.cover = cover

        # Look up authors attached to the book
        cursor.execute('SELECT author_id FROM books_authors WHERE book_id=' + str(book_key))
        for author_id in cursor:
            auth_id.append(author_id[0])

        # Look up author details
        for (auth) in auth_id:
            cursor.execute('SELECT name FROM authors WHERE id=' + str(auth))
            for name in cursor:
                book_object.author.append(name[0])

        book_objects.append(book_object.toJson())

    cursor.close()
    conn.close()
    response_object['books'] = book_objects
    return jsonify(response_object)


@app.route('/user/<user_id>', methods=['GET'])
def all_users(user_id):
    response_object = {'status': 'success'}
    user = None
    conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            passwd=PASSWD,
            database=DATABASE
        )
    cursor = conn.cursor()

    # ADD ERROR: if more than one user is found
    cursor.execute('SELECT name, email, location, profile_photo FROM readers where id=' + str(user_id))
    for (name, email, location, photo) in cursor:
        user = {
            'name': name,
            'email': email,
            'location': location,
            'profile_photo': photo
        }
    response_object['user'] = user
    return jsonify(response_object)

@app.route('/posts', methods=['GET', 'POST'])
def all_posts():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        POSTS.insert( 0, {
            'id': uuid.uuid4().hex,
            'timestamp': datetime.now(),
            'message': post_data.get('data')
        })
    else:
        response_object['posts'] = POSTS
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
