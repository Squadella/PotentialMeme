from django.contrib import admin
from .models import Post, Comment, UpVote, Favorite

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UpVote)
admin.site.register(Favorite)