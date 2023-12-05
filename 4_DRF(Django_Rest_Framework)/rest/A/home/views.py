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

from rest_framework.views import APIView
from rest_framework.response import Response

class Home(APIView):
    def get(self, request):
        return Response({"name":"jack"})