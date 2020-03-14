from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import HistoryNode, ReferringFlow


def index(request):
    # TODO: Get entire HistoryNode, ReferringFlow list, not ordered by anything.
    node_list = HistoryNode.objects
    edge_list = ReferringFlow.objects
    template = loader.get_template('sciencehistory/stic.html')
    context = {
        'node_list' : node_list,
        'edge_list' : edge_list
    }
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'sciencehistory/index.html')