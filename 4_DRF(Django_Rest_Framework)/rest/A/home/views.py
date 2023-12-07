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

# from rest_framework.views import APIView
# from rest_framework.response import Response
# class Home(APIView):
#         name= request.query_params['name']
#         return Response({"name": name})
# ___________________________________
#POST
# sample usage: file uploadding
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# class Home(APIView):
#     def get(self, request):
#         name= request.query_params['name']
#         return Response({"name": name})
#
#     def post(self, request):
#         name= request.data['name']
#         return Response({"name": name})

#----------------------------------------------
#session 3

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Person
# from .serializers import PersonSerializer
#
# class Home(APIView):
#     def get(self, request):
#         # persons= Person.objects.all()
#         persons= Person.objects.get(name='zahra')
#         ser_data= PersonSerializer(instance=persons)
#         # ser_data= PersonSerializer(instance=persons, many= True)
#         return Response(data= ser_data.data)
#------------------------------------------------
# Session 4

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Person, Question, Answer
from rest_framework import status


class Home(APIView):
    # permission_classes = [IsAuthenticated,]
    permission_classes = [IsAdminUser,]
    def get(self, request):
        # persons= Person.objects.all()
        persons= Person.objects.all()
        ser_data= PersonSerializer(instance=persons, many= True)
        # ser_data= PersonSerializer(instance=persons, many= True)
        return Response(data= ser_data.data)


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True)
        return Response(srz_data.data, status= status.HTTP_200_OK)

    def post(self, request):
        srz_data= QuestionSerializer(data= request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk): #update
        question = Question.objects.get(pk=pk)
        srz_data= QuestionSerializer(instance=question, data= request.data, partial= True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status= status.HTTP_200_OK)
        return Response(srz_data.errors, status= status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message': 'question deleted'}, data= status.HTTP_200_OK)
