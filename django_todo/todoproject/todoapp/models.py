from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    due_date = models.DateField()
    created_date = models.DateField(default=timezone.now)
    completed_date = models.DateField(null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)