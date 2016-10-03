from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.CharField(max_length=1000)

class Comment(models.Model):
    content = models.CharField(max_length=10000)
    post = models.ForeignKey(Post)