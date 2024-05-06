from typing import Any
from django.db import models
from django.utils import timezone

# Create your models here.

class CarManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)

class Car(models.Model):
    name=models.CharField(max_length=20)
    color=models.CharField(max_length=8)
    brand=models.CharField(max_length=20)
    style_body=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    description=models.TextField(default='')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True)

    objects = CarManager()

    def delete(self):
        self.deleted_at=timezone.now()
        self.save()