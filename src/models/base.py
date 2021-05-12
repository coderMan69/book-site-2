from booksite import db


class BaseModel(db.Model):

    id = db.Column(db.Interger, autoincrement=True, primary_key=True)
