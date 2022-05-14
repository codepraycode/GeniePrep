from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.


class IndexView(APIView):
    

    def get(self, request, format=None):
        
        return Response({"Message": 'Hello World!'}, status=status.HTTP_200_OK);
