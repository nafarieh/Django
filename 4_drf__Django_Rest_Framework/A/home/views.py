# query params in http://127.0.0.1:8000/?name=zahra

from rest_framework.views import APIView
from rest_framework.response import Response
class Home(APIView):
    def get(self, request):
        return Response({"name": 'jack'})

    def post(self, request):
        name= request.data['name']
        return Response({"name": name})