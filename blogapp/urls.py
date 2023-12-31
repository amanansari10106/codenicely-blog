from django.urls import path

from blogapp import apis


urlpatterns = [
    path("create/", apis.CreateBlogAPI.as_view(), name="createBlogAPI"),
    path("blog/<int:blogID>/", apis.GetBlogAPI.as_view(), name="getBlogAPI"),
    path("comment/", apis.CreateCommentAPI.as_view(), name="createCommentAPI"),
    path("list/", apis.ListBlogAPI.as_view(), name="listBlogAPI"),
    path("comments/<int:blogID>/", apis.ListCommentsAPI.as_view(), name="listCommentsAPI"),
    path("delete/<int:blogID>/", apis.DeleteBlogAPI.as_view(), name="deleteBlogAPI"),
    path("edit/<int:blogID>/", apis.EditBlogAPI.as_view(), name="editBlogAPI"),
    path("comment/edit/<int:commentID>/", apis.EditCommentAPI.as_view(), name="editCommentAPI"),
    path("comment/delete/<int:commentID>/", apis.DeleteCommentAPI.as_view(), name="editCommentAPI")
# sdfsdfd
]