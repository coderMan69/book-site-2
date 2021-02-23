from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

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
        'cover': 'require(../assets/photos/mobyDick.jpeg)',
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Adventures of Huckleberry Finn',
        'author': ['Mark Twain'],
        'cover': '../assets/photos/huckFinn.jpg',
    }
]

POSTS = [
    {
        'id': uuid.uuid4().hex,
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
            'author': post_data.get('author')
        })
        # response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

@app.route('/posts', methods=['GET', 'POST'])
def all_posts():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        POSTS.append({
            'id': uuid.uuid4().hex,
            'message': post_data.get('data')
        })
    else:
        response_object['posts'] = POSTS
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
