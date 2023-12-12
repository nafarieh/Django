from django.shortcuts import render
from django.shortcuts import render
from django.views import View

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'PUT'])
def home(request):
    return Response({'name':'amir'})