from django.contrib import admin
from .models import HistoryNode
from .models import ReferringFlow

# Register your models here.
admin.site.register(HistoryNode)
admin.site.register(ReferringFlow)