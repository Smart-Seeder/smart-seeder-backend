from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Crop
from .classification_ss import predict_crop
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import CropDataSerializer
# Create your views here.
@api_view(['POST'])
def add_crop(request):
    serializer = CropDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_crops(request):
    crops = Crop.objects.all()
    serializer = CropDataSerializer(crops, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_crop(request, pk):
    crop = Crop.objects.get(id=pk)
    serializer = CropDataSerializer(crop, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_plate(request, pk):
    try:
        crop = Crop.objects.get(id=pk)
        name = crop.name
        seed_plate_id, fertilizer_plate_id, seed_size = predict_crop(name)
        
        seed_plate_id = int(seed_plate_id)
        fertilizer_plate_id = int(fertilizer_plate_id)
        depth_of_seed = 2*seed_size
        
        return JsonResponse({
            'seed_plate_id': seed_plate_id,
            'fertilizer_plate_id': fertilizer_plate_id,
            'depth_of_seed': depth_of_seed
        })
    except Crop.DoesNotExist:
        return JsonResponse({'error': 'Crop not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

import requests

def fetch_realtime_data(request):
    url = 'https://seeder-db-default-rtdb.firebaseio.com/.json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch data from Firebase Realtime Database'}, status=500)
