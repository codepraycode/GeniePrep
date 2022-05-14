from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.http import JsonResponse

# Models
from .models import Users
#  Serializers
from .serializers import UserSerializer, LoginSerializer

## Renderers
# from .renderers import UserAccountRenderer

# Create your views here.


class LogInView(APIView):
    # METHODS: POST
    serializer_class = LoginSerializer

    def post(self, request):
        # user = request.data
        serializer = self.serializer_class(data=request.data)
        # should raise error 400 on exception
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

class LogOutUser(APIView):
    # METHODS: GET
    pass


class UsersView(ListCreateAPIView):
    # METHODS: POST, GET, PUT
    serializer_class = UserSerializer
    # renderer_classes = (UserAccountRenderer,)
    queryset = Users.objects.all()
    
    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        
        return serializer.save()
    
    def get_queryset(self):
        return self.queryset.all()


class UserView(GenericAPIView):
    """
    View for a particular user
    
    """
    serializer_class = UserSerializer
    
    def get(self, req):
        matric_number = req.GET.get('m', None)
        
        
        if matric_number is None:
            return Response({'message': 'No Matric Number in request parameter'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = Users.objects.get(matric_number=matric_number)
        except:
            return Response({'message': 'No User Found'}, status=status.HTTP_404_NOT_FOUND)
        
        res = {
            'matric_number': user.matric_number,
            'email': user.email,
            'first_name': user.first_name,
            'surname': user.surname,
        }
        
        return Response(res, status=status.HTTP_200_OK)
  
        
