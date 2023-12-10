from app import db
from uuid import uuid4

def generate_uuid():
    return str(uuid4())

class Posts(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text())
    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    

    def __init__(self, title, description):
        self.title = title
        self.description = description