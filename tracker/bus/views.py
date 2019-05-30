from django.shortcuts import render
import googlemaps
from django.http import HttpResponse
import json

def map_bus(request):
    """
    Testing sphinx documentation:
    Method currently supports only GET method.

    """

    if(request.method == 'GET'):
        return render(request, 'static/map.html')
    else:
        return HttpResponse(json.dumps({'status' : 'request method not supported currently'}))
