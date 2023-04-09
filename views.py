from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import clientss
from . serializers import clientssSerializer


class clientssList(APIView):

    def get(self, request):
        clients1=clientss.objects.all()
        serializer=clientssSerializer(clients1, many=True)

        return Response(serializer.data)
    def post(self):
        pass