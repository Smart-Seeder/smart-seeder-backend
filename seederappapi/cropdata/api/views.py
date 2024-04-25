from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from cropdata import models
from . import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# function based view
@api_view(['GET'])
def get_crops(request):
    crops = models.Crop.objects.all()
    serializer = serializers.CropDataSerializer(crops, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def get_plate(request, pk):
#     crop = models.Crop.objects.get(pk=pk)
#     name = crop.name
#     result =  predict_plate(name)
#     print(result)
#     return Response({'result': 'result'})