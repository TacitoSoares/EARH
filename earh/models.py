from django.db import models

# Create your models here.

class Post(models.Model):
    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)