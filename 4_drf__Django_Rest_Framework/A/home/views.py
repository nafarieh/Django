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
    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass