from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_marshmallow import Marshmallow
import re

app = Flask(__name__)

# prod db
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://aklmxjsdqjwmlj:bfc4496f12fdd618d86d092b25d8dea9cde23a12c11d416ffb1589fd640f02bf@ec2-52-73-155-171.compute-1.amazonaws.com:5432/de3nk8v0847kgr"

# Dev DB
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blogdb.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from models.posts import PostModel
from models.schemas import posts_schema, post_schema


@app.get('/')
def home():
	return redirect(url_for('get_all_posts'))


@app.get('/api/posts/')
def get_all_posts():
	response = posts_schema.jsonify(PostModel.query.all())
	return response, 200


@app.post('/api/posts/')
def add_post():
	payload = PostModel(
		title=request.json.get('title'),
		body=request.json.get('body'),
		author=request.json.get('author'),
		featured=request.json.get('featured')
	)
	try:
		db.session.add(payload)
		db.session.commit()
		return post_schema.jsonify(payload), 201
	except IntegrityError:
		db.session.rollback()
		return {'message': 'duplicate post found!'}, 409


@app.get('/api/posts/<int:pk>')
def get_post(pk):
	response = post_schema.jsonify(PostModel.query.get(pk))
	if response:
		return response, 200
	return {'message': 'not found'}, 404
	

@app.patch('/api/posts/<int:pk>')
def update_post(pk):
	payload = request.json
	query = PostModel.query.get_or_404(pk)
	if 'title' in payload:
		query.title = payload['title']
		query.slug = re.sub('[ ]', '-', payload['title'].lower())
	elif 'body' in payload:
		query.body = payload['body']
	elif 'featured' in payload:
		query.featured = payload['featured']
	elif 'author' in payload:
		query.author = payload['author']
	db.session.commit()
	return post_schema.jsonify(query), 200


@app.delete('/api/posts/<int:pk>')
def delete_post(pk):
	post = PostModel.query.get_or_404(pk)
	db.session.delete(post)
	db.session.commit()
	return {}, 204


if __name__ == '__main__':
	app.run()
