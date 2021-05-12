from booksite import db
from base import BaseModel


class Books(BaseModel):

    title = db.Column(db.String(512), nullable=False)
    cover = db.Column(db.String(512), nullable=False)
    rating = db.Column(db.Float)
    num_of_rating = db.Column(db.Integer)
    downloads = db.Column(db.String(4096))

    def __repr__(self):
        return f"Book({self.title})"
