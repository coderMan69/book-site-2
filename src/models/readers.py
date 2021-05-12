from booksite import db
from base import BaseModel


class Readers(BaseModel):

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    profile_photo = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"Reader(ID: {self.id}, Name: {self.name}, Email: {self.email})"
