from django.shortcuts import render
from .serializer import Studentserilaiser
from .models import Student
from rest_framework.response import Response
from rest_framework import status,viewsets



class Student_view(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserilaiser
    

    

    
    


        


        




# Create your views here.
