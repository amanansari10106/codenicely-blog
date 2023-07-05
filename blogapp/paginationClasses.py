from rest_framework.pagination import PageNumberPagination

class listBlogPaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = "records"
    max_page_size = 50
    
class listCommentPaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = "records"
    max_page_size = 50