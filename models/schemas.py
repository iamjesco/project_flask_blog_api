from app import ma


class PostSchema(ma.Schema):
	class Meta:
		fields = ('pk', 'title', 'slug', 'body', 'created', 'author', 'featured', 'updated')
		

post_schema = PostSchema()
posts_schema = PostSchema(many=True)



