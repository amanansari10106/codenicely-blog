from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

class CommentModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    body = models.TextField()
    postedAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    