from django.db import models

# Create your models here.
class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='crops/', default='crops/default.jpeg')

    def __str__(self):
        return self.name