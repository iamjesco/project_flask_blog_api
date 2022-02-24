from flask import Flask, redirect, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config["SECRET_KEY"] = '34gfdesy4567yweryh'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blogdb.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from models.posts import PostModel
from models.schemas import posts_schema, post_schema


# Wrong route handler function
@app.errorhandler(400)
def page_not_found(e):
	return {'message': 'that route does not exist'}, 400


#   Route to get all posts
@app.get('/')
def home():
	return redirect(url_for('get_all_posts'))


@app.get('/api/posts/')
def get_all_posts():
	query = PostModel.query.all()
	result = posts_schema.dump(query)
	return jsonify(result.data), 200


#   Route to create a post
@app.post('/api/posts/')
def add_post():
	new_post = PostModel(
		title=request.json.get('title'),
		content=request.json.get('content')
	)
	db.session.add(new_post)
	db.session.commit()
	return post_schema.jsonify(new_post), 201


#   Route to get a single post
@app.get('/api/posts/')
def get_post(pk):
	single_post = PostModel.query.get(pk)
	if single_post:
		return post_schema.jsonify(single_post), 200
	return {'message': 'not found'}, 404
	

#   Route to update a post
@app.put('/api/posts/<int:pk>/')
def update_post(pk):
	updated_post = PostModel.query.get(pk)
	#   data received from request
	title = request.json.get('title')
	content = request.json.get('content')
	# new data sent as update
	updated_post.title = title
	updated_post.content = content
	#   submit to db
	db.session.commit()
	return post_schema.jsonify(updated_post), 200


#   Rout to delete a post
@app.delete('/api/posts/<int:pk>/')
def delete_post(pk):
	single_post = PostModel.query.get(pk)
	db.session.delete(single_post)
	db.session.commit()
	return {'message': f'post with pk {pk} deleted!'}, 204


if __name__ == '__main__':
	app.run()
