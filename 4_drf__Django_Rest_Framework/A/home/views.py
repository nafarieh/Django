from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer #, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Person #, Question, Answer
from rest_framework import status


class Home(APIView):
    # permission_classes = [IsAuthenticated,]
    permission_classes = [IsAdminUser,]
    def get(self, request):
        persons= Person.objects.all()
        ser_data= PersonSerializer(instance=persons, many= True)
        # ser_data= PersonSerializer(instance=persons, many= True)
        return Response(data= ser_data.data)
