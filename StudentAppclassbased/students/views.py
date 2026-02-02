from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from students.seraializers import StudentSerializer
from students.models import Student
from rest_framework import status
from rest_framework.views import APIView
class Studentlist(APIView):

    def get(self,request):
        s=Student.objects.all() #read all student records
        stu=StudentSerializer(s,many=True) #serialize these records into json objects
        return Response(stu.data,status=status.HTTP_200_OK) # sends the response back to Client side with status code 200
        
    def post(self,request):
        s=StudentSerializer(data=request.data) # deserialize the json format data into django format using serializer class
        if s.is_valid(): # checks whether data is valid or not
            s.save() # if valid saves the data into table
            return Response(s.data,status=status.HTTP_201_CREATED) # sends created record as response with status code 201
        

from django.http import Http404

class Studentdetail(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self,request,pk):
        s=self.get_object(pk)
        stu=StudentSerializer(s)
        return Response(stu.data,status=status.HTTP_200_OK)