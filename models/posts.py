from app import db
from datetime import datetime
import re


class PostModel(db.Model):
	pk = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), unique=True, nullable=False)
	slug = db.Column(db.String(200), unique=True, nullable=False)
	body = db.Column(db.Text, nullable=False)
	created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	updated = db.Column(db.DateTime(), onupdate=datetime.utcnow)
	author = db.Column(db.String(50), default='Uncle Jesco')
	featured = db.Column(db.Boolean, default=False)
	
	def __repr__(self):
		return f'{self.title}'
	
	def __init__(self, title, body, author, featured):
		self.title = title
		self.body = body
		self.author = author
		self.featured = featured
		self.slug = re.sub('[ ]', '-', self.title.lower())

