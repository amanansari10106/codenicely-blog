from django.contrib import admin

# Register your models here.
from blogapp.models import BlogModel, CommentModel

admin.site.register(BlogModel)
admin.site.register(CommentModel)