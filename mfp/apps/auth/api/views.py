from django.http import HttpResponse
from rest_framework import generics
from django.contrib.auth.models import User
from apps.auth.api.serializers import RegisterSerializer


class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
