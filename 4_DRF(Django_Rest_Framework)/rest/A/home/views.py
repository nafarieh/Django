# from django.shortcuts import render
# from django.views import View
#
# # Create your views here.
#
# class Home(View):
#     def get(self, request):
#         return render(request,'home/home.html')

#--------------------------------------------
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# @api_view(['GET', 'POST', 'PUT'])
# def home(request):
#     return Response({'name':'amir'})
#--------------------------------------------

# from rest_framework.views import APIView
# from rest_framework.response import Response
#
# class Home(APIView):
#     def get(self, request):
#         return Response({"name":"jack"})

#-----------------------------------------------
# http://127.0.0.1:8000/zahra

# from rest_framework.views import APIView
# from rest_framework.response import Response
# class Home(APIView):
#     def get(self, request,name):
#         return Response({"name": name})

#-----------------------------------------------
# query parameter in http://127.0.0.1:8000/?name=zahra

# from rest_framework.views import APIView
# from rest_framework.response import Response
# class Home(APIView):
#     def get(self, request):
#         name= request.GET['name']
#         return Response({"name": name})

#--------------------------------------------
# query params in http://127.0.0.1:8000/?name=zahra

from rest_framework.views import APIView
from rest_framework.response import Response
class Home(APIView):
    def get(self, request):
        name= request.query_params['name']
        return Response({"name": name})
# ___________________________________
#POST
# sample usage: file uploadding

from rest_framework.views import APIView
from rest_framework.response import Response
class Home(APIView):
    def get(self, request):
        name= request.query_params['name']
        return Response({"name": name})

    def post(self, request):
        name= request.data['name']
        return Response({"name": name})