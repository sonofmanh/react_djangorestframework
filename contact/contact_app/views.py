from django.shortcuts import render

#  our own view properties imported below

from .models import Messages
from .serializers import Messageserializer
from rest_framework import viewsets
# Create your views here.


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = Messageserializer