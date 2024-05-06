from django.db import models
from django.utils import timezone
from cars.models import Car

# Create your models here.

class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)

class Comment(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )

    context=models.TextField(max_length=250, default='')
    created_at=models.DateTimeField(auto_now_add=True)
    deleted_at=models.DateTimeField(null=True)

    objects = CommentManager()

    def delete(self):
        self.deleted_at=timezone.now()
        self.save()