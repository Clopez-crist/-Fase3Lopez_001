from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Game(models.Model):
    nombre = models.CharField(max_length=100)
    creador = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    cod= models.UUIDField(primary_key=True, default=uuid.uuid4)