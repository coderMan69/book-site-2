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
        self.id = ''
        self.title = ''
        self.author = []
        self.cover = ''
        self.read = ''
        self.reading = ''

    def __init__(self, id, read, reading):
        self.id = id
        self.title = ''
        self.author = []
        self.cover = ''
        self.read = read
        self.reading = reading

    def toJson(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    def print(self):
        print("Id: " + str(self.id) +
              "\nTitle: " + str(self.title) +
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
        book_object = Book(book_key, book[1], book[2])

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


@app.route('/readers/<user_id>', methods=['GET'])
def get_readers(user_id):
    response_object = {'status': 'success'}
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        database=DATABASE
    )
    cursor = conn.cursor()
    user = None
        # ADD ERROR: if more than one user is found
    cursor.execute('SELECT * FROM readers WHERE id=' + str(user_id))
    for (id, name, email, location, photo) in cursor:
        user = {
            'id': id,
            'name': name,
            'email': email,
            'location': location,
            'profile_photo': photo
        }
    response_object['user'] = user
    cursor.close()
    conn.close()
    return jsonify(response_object)

@app.route('/readers', methods=['PUT'])
def update_readers():
    response_object = {'status': 'success'}
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        database=DATABASE
    )
    cursor = conn.cursor()
    put_data = request.get_json()
    cursor.execute("UPDATE readers SET name = '" + str(put_data.get('name')) +
                    "', email = '" + str(put_data.get('email')) +
                    "', location = '" + str(put_data.get('location')) +
                    "' WHERE id = " + str(put_data.get('id')))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(response_object)

@app.route('/reader_book/<user_id>/<book_id>', methods=['GET'])
def get_readers_authors(user_id, book_id):
    response_object = {'status': 'success'}
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        database=DATABASE
    )
    cursor = conn.cursor()
    cursor.execute('SELECT red, reading FROM readers_books WHERE reader_id = ' + str(user_id) +
                   ' and book_id = ' + str(book_id))            
    # Should only be one match
    for (read, reading) in cursor:
        book_info = {
            'read': read,
            'reading': reading,
        }
    
    response_object['read'] = book_info['read']
    response_object['reading'] = book_info['reading']
    cursor.close()
    conn.close()
    return jsonify(response_object)

@app.route('/reader_book', methods=['PUT'])
def update_readers_authors():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        database=DATABASE
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE readers_books SET red = '" + str(post_data.get('read')) +
                   "', reading = '" + str(post_data.get('reading')) +
                   "' WHERE reader_id = " + str(post_data.get('reader_id')) +
                   " and book_id = " + str(post_data.get('book_id')))
    conn.commit()
    cursor.close()
    conn.close()
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
