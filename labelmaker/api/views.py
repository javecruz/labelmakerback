from django.shortcuts import render
from rest_framework import viewsets

from .models import Label
from .serializers import LabelSerializer


class LabelView(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
