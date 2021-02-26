from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
from datetime import datetime

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Moby Dick',
        'author': ['Herman Melville'],
        'cover': 'https://www.gutenberg.org/cache/epub/2701/pg2701.cover.medium.jpg',
        'read': '',
        'reading': 'true',
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Adventures of Huckleberry Finn',
        'author': ['Mark Twain'],
        'cover': 'https://www.gutenberg.org/cache/epub/76/pg76.cover.small.jpg',
        'read': 'true',
        'reading': '',
    }
]

POSTS = [
    {
        'id': uuid.uuid4().hex,
        'timestamp': datetime.now(),
        'message': 'Hello World',
    }
]

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'reading': post_data.get('reading'),
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
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
