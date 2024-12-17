from django.shortcuts import render
from rest_framework.decorators import api_view #import rest_framework.decorators
from rest_framework.response import Response #import rest_framework.response
from .models import *  #import models file
from .serializers import *  #import serializers file

#GET api
@api_view(['GET'])
def nk(request):
    obj = student.objects.all()
    serializer = studentserializer(obj,many = True)
    return Response ({'status' : 200 ,'message':'right' , 'payload' :serializer.data})


# @api_view(['GET'])
# def jojo(request):
#     obj = student1.objects.all()
#     serializer = studentserializer1(obj,many = True)
#     return Response ({'status' : 200 ,'massage':'right' , 'payload' : serializer.data})

#POST api
@api_view(['POST'])
def rk(request):
    data =request.data 
    serializer = studentserializer(data = request.data)
    if not serializer.is_valid():
        return Response ({'status' : 201 , 'message' : 'worng'})
    serializer.save()
    return Response({'status' : 200 ,'message' : 'right' , 'payload' :serializer.data})    

#PUT api
@api_view(["PUT"])
def nk1(request,id):
    try:
        obj = student.objects.get(id=id)
        serializer = studentserializer(obj,data = request.data)
        if not serializer.is_valid():
            return Response ({'status' : 201 , 'message' : 'worng'})
        serializer.save()
        return Response({'status' : 200 ,'message' : 'right' , 'payload' : serializer.data})    
    except Exception as a:
        return Response({'status' : 403 , 'message' : 'worng'})
    
 #PATCH api   
@api_view(['PATCH'])
def nk2(request,id):
    try:
        obj = student.objects.get(id=id)
        serializer = studentserializer(obj,data = request.data,partial = True)
        if not serializer.is_valid():
            return Response ({'status' : 201 , 'message' : 'worng'})
        serializer.save()
        return Response({'status' : 200 ,'message' : 'right' , 'payload' : serializer.data})    
    except Exception as a:
        return Response({'status' : 403 , 'message' : 'worng'})

#DELITE API
@api_view(['DELETE'])
def nk3(request,id):
    obj =student.objects.get(id=id)
    obj.delete()
    try :
        return Response({'status' : 200 ,'message' : 'right'})
    except Exception as a:
        return Response({'status' : 403 ,'message' : 'worng'})