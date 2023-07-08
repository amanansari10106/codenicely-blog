

from rest_framework.views import APIView
from blog.utils import cresponse
from blog import messages
from rest_framework.response import Response
from blogapp.serializers import CreateBlogModelSerializer, CreateCommentModelSerializer, ListBlogModelSerializer, ListCommentModelSerializer, GetBlogModelSerializer
from blogapp.paginationClasses  import listBlogPaginator, listCommentPaginator
from blogapp.models import BlogModel, CommentModel
from rest_framework.permissions import IsAuthenticated
class CreateBlogAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        print(request.data)
        print("Printing Data")
        serializer = CreateBlogModelSerializer(data=request.data, context={"request":request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(cresponse(True, message=messages.blogCreated, data=serializer.data))
        print(serializer.errors)
        return Response(cresponse(False, message=messages.serializerError, data=serializer.errors))
    
class GetBlogAPI(APIView):

    def get(self, request, blogID):
        if BlogModel.objects.filter(id=blogID).exists():
            blog = BlogModel.objects.get(id=blogID)
            serializer = GetBlogModelSerializer(blog, context={"request":request})
            return Response(cresponse(True, data=serializer.data))
        return Response(cresponse(False, message=messages.blogNotExist))        


class CreateCommentAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CreateCommentModelSerializer(data=request.data, context={"request":request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(cresponse(True, message=messages.commentCreated, data=serializer.data))
        return Response(cresponse(False, message=messages.serializerError, data=serializer.errors))
    
class ListBlogAPI(APIView):
    pagination_class = listBlogPaginator
    serializer_class = ListBlogModelSerializer
    def get(self, request):
        queryset = BlogModel.objects.all().order_by('-createdAt')
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(paginated_queryset, many=True, context={"request":request})
        # return Response(serializer.data)
        return Response(cresponse(True, message=messages.sucess, data=paginator.get_paginated_response(serializer.data).data))



class ListCommentsAPI(APIView):
    pagination_class = listCommentPaginator
    serializer_class = ListCommentModelSerializer
    def get(self, request):
        blog = BlogModel.objects.get(id=request.GET.get("blogID"))
        queryset = CommentModel.objects.filter(blog=blog)
        print(request.GET.get('blogID'))
        print(queryset)
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(paginated_queryset, many=True, context={"request":request})
        # return Response(serializer.data)
        return Response(cresponse(True, message=messages.sucess, data=paginator.get_paginated_response(serializer.data).data))
    
class DeleteBlogAPI(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, blogID):
        blog = BlogModel.objects.get(id=blogID)
        if request.user == blog.user:
            blog.delete()
            return Response(cresponse(True, message=messages.blogDeleted))
        else:
            return Response(cresponse(False, message=messages.notAuthorized))




