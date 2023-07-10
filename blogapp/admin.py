from django.contrib import admin

# Register your models here.
from blogapp.models import BlogModel, CommentModel
from usersapp.models import TestModel
admin.site.register(BlogModel)
admin.site.register(CommentModel)
admin.site.register(TestModel)