from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

class ListView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends=[SearchFilter]
    #search_fields = ['city'] 
    search_fields = ['^name'] 
