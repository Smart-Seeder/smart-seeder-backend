from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Crop

# Create your views here.

def add_crop(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        crop = Crop(name=name, image=image)
        crop.save()
    return JsonResponse({'status': 'crop added successfully'})

def get_crops(request):
    crops = Crop.objects.all()
    crop_list = []
    for crop in crops:
        crop_list.append({'name': crop.name, 'image': crop.image.url})
    return JsonResponse(crop_list, safe=False)

def get_crop(request, pk):
    crop = Crop.objects.get(id=pk)
    return JsonResponse({'name': crop.name, 'image': crop.image.url})