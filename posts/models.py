from datetime import datetime

from django.db.models import *


class Post(Model):
    title = CharField(max_length=250, help_text='Введите название поста')
    author = CharField(max_length=100)
    post_body = TextField(help_text='Введите текст поста сюда')
    published_date = DateTimeField(default=datetime.now)
    class Meta:
        ordering = ['author']


class Comment(Model):
    author = CharField(max_length=100)
    comment_body = CharField(max_length=500)
    post = ForeignKey(Post, on_delete=CASCADE)
    create_data = DateTimeField(default=datetime.now)

