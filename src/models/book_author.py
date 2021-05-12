from booksite import db


class BookAuthor(db.Model):

    book_id = db.Column(db.Interger)
    author_id = db.Column(db.Integer)


    
