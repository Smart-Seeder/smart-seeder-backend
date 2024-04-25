from rest_framework import serializers
from cropdata.models import Crop

class CropDataSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Crop
        fields = ('id', 'name', 'image')