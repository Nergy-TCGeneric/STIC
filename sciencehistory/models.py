import datetime

from django.db import models
from django.utils import timezone

class HistoryNode(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=100, default="http://stic.dothome.co.kr/w/")
    created_date = models.DateTimeField("Created time", auto_now_add=True)
    modified_date = models.DateTimeField("Modified time", default=timezone.now)

    def __str__(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def is_recently_modified(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.modified_date <= now

class ReferringFlow(models.Model):
    start = models.PositiveIntegerField(default=0)
    end = models.PositiveIntegerField(default=0)
    indirect = models.BooleanField(default=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    def get_startpoint(self):
        return self.start

    def get_endpoint(self):
        return self.end

    def is_indirect_reference(self):
        return self.indirect