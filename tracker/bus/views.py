from django.shortcuts import render
import googlemaps
from django.http import HttpResponse
import json

def map_bus(request):
    """ Function used to locate a point on the map.

    The function only supports GET method for now. The points to be located are fixed for now.
    The arguments mentioned below are for future use.

    Args:
        latitude (int): Latitude of vehicle to locate.
        longitude (int) : Longitude of vehicle to locate.

    Returns:
        html: renders a html containing the location of the vehicle on a map.

    """

    if(request.method == 'GET'):
        return render(request, 'static/map.html')
    else:
        return HttpResponse(json.dumps({'status' : 'request method not supported currently'}))
