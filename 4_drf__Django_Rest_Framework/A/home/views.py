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


class QuestionListView(APIView):
    """
    read question
    """
    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True)
        return Response(srz_data.data, status= status.HTTP_200_OK)

class QuestionCreateView(APIView):
    """
        Create new question
    """
    def post(self, request):
        srz_data= QuestionSerializer(data= request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionUpdateView(APIView):
    """
    Update question
    """
    def put(self, request, pk): #update
        question = Question.objects.get(pk=pk)
        srz_data= QuestionSerializer(instance=question, data= request.data, partial= True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status= status.HTTP_200_OK)
        return Response(srz_data.errors, status= status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(APIView):
    """
    delete question
    """
    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message': 'question deleted'}, data= status.HTTP_200_OK)