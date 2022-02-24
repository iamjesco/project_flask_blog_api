from app import ma


class PostSchema(ma.Schema):
	class Meta:
		fields = ('pk', 'title', 'content', 'published')
		

post_schema = PostSchema(strict=True)
posts_schema = PostSchema(many=True, strict=True)
