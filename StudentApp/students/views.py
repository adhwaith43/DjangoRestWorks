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
        
#primary key based 
#Api for reading a specific record

@api_view(['GET','PUT','DELETE'])
def studentdetail(request,pk):
    #First read the student record from the Student Table
    try:
        s=Student.objects.get(pk=pk)
    except:#if student object does not exist
        return Response({'message':'student does not exist'},status=status.HTTP_404_NOT_FOUND)
    
    if (request.method=='GET'): #if the request method coming from client side is get


        stu=StudentSerializer(s) #converts the student object into json format
        return Response(stu.data,status=status.HTTP_200_OK) #send the response back to the client

    if (request.method=="PUT"): #if the request is PUT
        stu=StudentSerializer(s,data=request.data) 
        if stu.is_valid(): 
            stu.save() 
            return Response(stu.data,status=status.HTTP_201_CREATED)
        
    if (request.method =="DELETE"):
        s.delete()
        return Response({'message':'student record is deleted'},status=status.HTTP_204_NO_CONTENT)
     

## mixins##

from rest_framework import mixins,generics

class Studentlist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)