from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import*
from .serializers import*

@api_view(['GET'])
def raj(request):
    obj=stud.objects.all()
    serializer=studserializer(obj,many = True)
    return Response({'status':200 , 'message' : 'right', 'payload':serializer.data})


@api_view(['POST'])
def rajj(request):
    data=request.data
    serializer=studserializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':201, 'massage':'wrong'})
    serializer.save()
    return Response({'status': 200, 'massage': 'right', 'payload':serializer.data})


@api_view(['PUT'])
def raj2(request,id):
    try:
        obj=stud.objects.get(id= id)
        serializer=studserializer(obj,data=request.data)
        if not serializer.is_valid():
          return Response({'status':201, 'massage':'wrong'})
        serializer.save()
        return Response({'status': 200, 'massage': 'right', 'payload':serializer.data})
    except Exception as a:
        return Response({'status':403, 'massage':'wrong'})


@api_view(['PATCH'])
def raj3(request,id):
    try:
        obj=stud.objects.get(id=id)
        serializer=studserializer(obj,data=request.data , partial = True)
        if not serializer.is_valid():
          return Response({'status':201, 'massage':'wrong'})
        serializer.save()
        return Response({'status': 200, 'massage': 'right', 'payload':serializer.data})
    except Exception as a:
        return Response({'status':403, 'massage':'wrong'})
    
@api_view(['DELETE'])
def raj4(request,id):
    obj=stud.objects.get(id=id)
    obj.delete()
    try:
        return Response ({'status':200 , 'massage':"right"})
    except Exception as a:
        return Response ({'status': 403 , 'massage':'wrong'})
    



    
    