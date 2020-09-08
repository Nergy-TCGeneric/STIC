from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import HistoryNode, ReferringFlow


def index(request):
    node_list = HistoryNode.objects.all()
    edge_list = ReferringFlow.objects.all()
    template = loader.get_template('sciencehistory/stic.html')
    context = {
        'node_list' : node_list,
        'edge_list' : edge_list
    }
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'sciencehistory/index.html')