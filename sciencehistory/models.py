import datetime

from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy
from django.db import models
from django.utils import timezone

class Significance(models.IntegerChoices):
    LOWEST = '1', gettext_lazy("Lowest")
    LOW = '2', gettext_lazy("Low")
    MODEREATE = "3", gettext_lazy("Moderate")
    HIGH = "4", gettext_lazy("High")
    HIGHEST = "5", gettext_lazy("Highest")

class Category(models.Model):
    title = models.CharField(max_length=100)
    color = ColorField(default="#FF0000")

    def __str__(self):
        return self.title

class HistoryNode(models.Model):
    title = models.CharField(max_length=100, unique=True, default="default")
    significance = models.IntegerField(choices=Significance.choices, default=Significance.MODEREATE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

class ReferringFlow(models.Model):
    start = models.ForeignKey(HistoryNode, on_delete=models.CASCADE, default=None, related_name="startpoint")
    end = models.ForeignKey(HistoryNode, on_delete=models.CASCADE, default=None, related_name="endpoint")
    indirect = models.BooleanField(default=False)
    description = models.CharField(max_length=200)
    significance = models.IntegerField(choices=Significance.choices, default=Significance.MODEREATE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.description