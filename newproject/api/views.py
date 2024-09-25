from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

# Create your views here.

@api_view(["GET","PUT","DELETE"])
def user_detail(request,pk): #pk = primary key
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response("User Isnot Found", status=status.HTTP_404_NOT_FOUND)
    

    if (request.method == "GET"):
        return Response(UserSerializer(user).data,status=status.HTTP_200_OK)
    
    if(request.method == "PUT"):
        serializerformethodput = UserSerializer(user, request.data)
        if serializerformethodput.is_valid():
            serializerformethodput.save()
            return Response(serializerformethodput.data)
        return Response("Error",status=status.HTTP_400_BAD_REQUEST)

    if (request.method == "DELETE"):
        user.delete()
        return Response("Deleted",status=status.HTTP_200_OK)    

@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


