from django.urls import path

from blogapp import apis


urlpatterns = [
    path("create/", apis.CreateBlogAPI.as_view(), name="createBlogAPI"),
    path("comment/", apis.CreateCommentAPI.as_view(), name="createCommentAPI"),
    path("list/", apis.ListBlogAPI.as_view(), name="listBlogAPI"),
    path("comments/", apis.ListCommentsAPI.as_view(), name="listCommentsAPI"),
    path("delete/<int:blogID>/", apis.DeleteBlogAPI.as_view(), name="deleteBlogAPI"),

]