from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.seraializers import StudentSerializer
from students.models import Student
from rest_framework import status




#API VIEW reading all student records

@api_view(['GET','POST'])
def studentlist(request):
    s=Student.objects.all()
    if (request.method == 'GET'):
        s=Student.objects.all() #read all student records
        stu=StudentSerializer(s,many=True) #serialize these records into json objects
        return Response(stu.data,status=status.HTTP_200_OK) # sends the response back to Client side with status code 200
    
    if (request.method =='POST'):
        s=StudentSerializer(data=request.data) # deserialize the json format data into django format using serializer class
        if s.is_valid(): # checks whether data is valid or not
            s.save() # if valid saves the data into table
            return Response(s.data,status=status.HTTP_201_CREATED) # sends created record as response with status code 201