from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer
from rest_framework import status
# Create your views here.
class UserRegister(APIView):
    def post(self, request):
        ser_data= UserRegisterSerializer(data= request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status= status.HTTP_201_CREATED)
        return Response(ser_data.errors, status= status.HTTP_400_BAD_REQUEST)


a= {'username':'amir', 'email':'amir@email.com', 'password':'amir' , 'password2':'amir'}