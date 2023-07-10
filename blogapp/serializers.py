


from rest_framework import serializers
from blogapp.models import BlogModel, CommentModel
import datetime
class CreateBlogModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogModel
        fields = ["id","user","title","body","description","createdAt"]

    def create(self, validated_data):
        user = self.context["request"].user
        
        return BlogModel.objects.create(**validated_data,user=user)
    
class CreateCommentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentModel
        fields = ["id","user","blog","body","postedAt"]

    def create(self, validated_data):
        user = self.context["request"].user
        blog = BlogModel.objects.get(id=self.context["request"].data["blogId"])
        return CommentModel.objects.create(**validated_data,user=user,blog=blog)
    
class ListBlogModelSerializer(serializers.ModelSerializer):

    is_author = serializers.SerializerMethodField()
    created_date = serializers.SerializerMethodField()
    created_time = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    def get_created_date(self, obj):
        date_string = obj.createdAt.strftime("%d/%m/%Y")
        return date_string
    def get_created_time(self, obj):
        time_string = obj.createdAt.strftime("%H-%M-%S")
        return time_string
    def get_is_author(self, obj):
        return obj.user == self.context["request"].user
    def get_author(self, obj):
        return obj.user.first_name

    class Meta:
        model = BlogModel
        fields = "__all__"

class ListCommentModelSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    def get_author(self, obj):
        return obj.user.first_name
    class Meta:
        model = CommentModel
        fields = "__all__"

class UpdateCommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"
class UpdateBlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = "__all__"

class GetBlogModelSerializer(serializers.ModelSerializer):
    is_author = serializers.SerializerMethodField()
    created_date = serializers.SerializerMethodField()
    created_time = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    def get_created_date(self, obj):
        date_string = obj.createdAt.strftime("%d/%m/%Y")
        return date_string
    def get_created_time(self, obj):
        time_string = obj.createdAt.strftime("%H-%M-%S")
        return time_string
    def get_is_author(self, obj):
        return obj.user == self.context["request"].user
    def get_author(self, obj):
        return obj.user.first_name
    class Meta:
        model = BlogModel
        fields = "__all__"