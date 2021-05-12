from booksite import db
from base import BaseModel


class Authors(BaseModel):

    name = db.Column(db.String(128), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    # If null assume author is still alive
    death_date = db.Column(db.Date)

    def __repr__(self):
        return f"Author({self.name})"
