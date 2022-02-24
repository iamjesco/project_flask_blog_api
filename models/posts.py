from app import db
from datetime import datetime


class PostModel(db.Model):
	pk = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), unique=True, nullable=False)
	content = db.Column(db.Text, nullable=False)
	published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	
	def __repr__(self):
		return f'{self.title}'
