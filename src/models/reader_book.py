from booksite import db


class ReaderBook(db.Model):

    reader_id = db.Column(db.Interger, db.ForeignKey('readers.id'), nullable=False)
    book_id = db.Column(db.Interger, db.ForeignKey('books.id'), nullable=False)
    # Use different ints as status 1: finished, 2: reading, etc.
    read_status = db.Column(db.Integer)
