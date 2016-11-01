from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField()
    isUpVoted = models.BooleanField(default=False)
    isFaved = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('images:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=10000)
    content = models.CharField(max_length=10000)

    def __str__(self):
        return self.content
