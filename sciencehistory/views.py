from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import HistoryNode


def index(request):
    node_list = HistoryNode.objects.order_by("-created_date")[:5]
    template = loader.get_template('sciencehistory/stic.html')
    context = {
        'historyNodeList' : node_list
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('sciencehistory/index.html')
    return HttpResponse(template.render(request))