from django.shortcuts import render

# Create your views here.
from usersapp.serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from usersapp.utils import test_password, validateEmail
from blog.utils import cresponse
from blog import messages
from usersapp.serializers import UserSerializer
class RegisterAPI(APIView):
    def post(self, request):
        name = request.data["name"]
        email = request.data["email"]
        password = request.data["password"]
        rePassword = request.data["rePassword"]
        test_pass = test_password(password, rePassword)
        test_email = validateEmail(email)
        if not test_email["success"]:
            return Response(cresponse(False, message=test_email["message"]))
        
        if not test_pass["success"]:
            return Response(cresponse(False, message=test_pass["message"]))
        
        if(User.objects.filter(email=email).exists()):
            return Response(cresponse(False, message=messages.emailUserAlreadyExist))
        user = User.objects.create_user(username=email, email=email, password=password, first_name = name)
        user.save()
        serializer = UserSerializer(user)
        return Response(cresponse(True, data=serializer.data, message="Success"))
        

class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data["email"]
                password = serializer.data["password"]
                user = authenticate(username=email, password=password)
                if user  is None:
                    return Response(cresponse(False, message=messages.wrongCreddentials))
                    
                refresh = RefreshToken.for_user(user)
                
                return Response(cresponse(True, data={"refresh":str(refresh), "access":str(refresh.access_token)}))

            
            return Response(cresponse(False, message=messages.serializerError, data=serializer.errors))
        
        except Exception as e:
            print(e)
            return Response({
                'status' : 400,
                "message" : "something went wrong",
                "data" : "dsd"
            })
from rest_framework_simplejwt.views import TokenRefreshView      
# class TestAPI(APIView):
class TestAPI(TokenRefreshView):
    def get(self, request):
        return Response({"user":request.user.username})

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Customize the response or add additional logic here
        return response