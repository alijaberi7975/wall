from rest_framework.parsers import MultiPartParser
from accounts.serializers import UserSerializer, UserRegisterSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ads.models import Ad
from ads.serializers import AdSerializer
from .models import User
from .permissions import IsUser


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAdListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
       instances = Ad.objects.filter(publisher=request.user)
       serializer = AdSerializer(instances, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)