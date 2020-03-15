import datetime

from django.db import models
from django.utils import timezone

class HistoryNode(models.Model):
    title = models.CharField(max_length=100, unique=True, default="default")

    def __str__(self):
        return self.title

class ReferringFlow(models.Model):
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    indirect = models.BooleanField(default=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description