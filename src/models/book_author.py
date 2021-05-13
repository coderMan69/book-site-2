from booksite import db


class BookAuthor(db.Model):

    book_id = db.Column(db.Interger, db.ForeignKey('books.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
