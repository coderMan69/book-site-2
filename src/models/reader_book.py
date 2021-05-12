from booksite import db


class ReaderBook(db.Model):

    reader_id = db.Column(db.Interger)
    book_id = db.Column(db.Integer)
    # Use different ints as status 1: finished, 2: reading, etc.
    read_status = db.Column(db.Integer)
