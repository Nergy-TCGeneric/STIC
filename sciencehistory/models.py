import datetime

from django.utils.translation import gettext_lazy
from django.db import models
from django.utils import timezone

class Significance(models.IntegerChoices):
    LOWEST = '1', gettext_lazy("Lowest")
    LOW = '2', gettext_lazy("Low")
    MODEREATE = "3", gettext_lazy("Moderate")
    HIGH = "4", gettext_lazy("High")
    HIGHEST = "5", gettext_lazy("Highest")

class HistoryNode(models.Model):
    title = models.CharField(max_length=100, unique=True, default="default")
    significance = models.IntegerField(choices=Significance.choices, default=Significance.MODEREATE)

    def __str__(self):
        return self.title

class ReferringFlow(models.Model):
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    indirect = models.BooleanField(default=False)
    description = models.CharField(max_length=200)
    significance = models.IntegerField(choices=Significance.choices, default=Significance.MODEREATE)

    def __str__(self):
        return self.description