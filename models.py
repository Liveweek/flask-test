from flask_sqlalchemy import SQLAlchemy


from routes import app
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    @property
    def serialize(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
            'age': self.age
        }
    