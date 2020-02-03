from django.shortcuts import render
# from rest_framework import generics
from employee_register.models import Employee
from .serialzers import SubjectSerializer
from rest_framework.viewsets import ModelViewSet


class SubjectListView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = SubjectSerializer


# class SubjectDetailView(generics.RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = SubjectSerializer
