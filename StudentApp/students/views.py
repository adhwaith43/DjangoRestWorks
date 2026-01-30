from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.models import Student




#API VIEW reading all student records

@api_view(['GET'])
def studentlist(request):
    s=Student.objects.all()
    if (request.method == 'GET'):
        s=Student.objects.all() #read all student records
        stu=StudentSerializer(s,many=True)
        return Response(stu.data,status=status.HTTP_200_OK)