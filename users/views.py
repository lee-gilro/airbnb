from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
from . import serializers

class Me(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(serializers.PrivateUserSerializer(user).data)

    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(
            user=user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class Users(APIView):
    def post(self, request):
        #암호에 대한 벨리데이션은 여기서 해야함.
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = serializers.PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PublicUser(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            raise NotFound
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)

    #사람들이 내 프로필에서 내 리뷰를 볼 수 있게 만든다.
    #
class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError

class LogIn(APIView):
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError

        user = authenticate(
            request=request,
            username=username,
            password=password,
            )
        if user:
            login(request=request, user=user)
            return Response({"ok" : "welcome"})
        else:
            return Response({"error":"wrong password"})

class LogOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok":"bye!"})