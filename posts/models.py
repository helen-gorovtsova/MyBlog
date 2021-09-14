from datetime import datetime

from django.db.models import *


class Post(Model):
    title = CharField(max_length=250)
    author = CharField(max_length=100)
    post_body = TextField()
    published_date = DateTimeField(auto_now_add=True)


class Comment(Model):
    author = CharField(max_length=100)
    comment_body = CharField(max_length=500)
    post = ForeignKey(Post, on_delete=CASCADE)
    create_data = DateTimeField(auto_now_add=True)


class Author(Model):
    pass
