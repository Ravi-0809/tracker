from django.shortcuts import render
import googlemaps
from django.http import HttpResponse
import json
from bus.models import Bus
# from rest_framework.views import APIView

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

# class map_vehicle(APIView):
#
#     def get(self, **kwargs):
#         institute_id = self.kwargs['institute_id']
#         bus_number = self.kwargs['bus_number']
#
#
#     def post(self, request, **kwargs):
#         institute_id = self.kwargs['institute_id']
#         bus_number = self.kwargs['bus_number']
#
#         try:
#             lat = request.POST.get('latitude')
#             long = request.POST.get('longitude')
#         except Exception as e:
#             return HttpResponse(json.dumps({'status' : 'unable to read POST data'}))
#
#         try:
#             qs = Bus.objects.filter(institute__institute_serial_number = institute_id).filter(bus_number = bus_number)
#             qs.latitude = lat
#             qs.longitude = long
#             qs.save()
#         except Exception as e:
#             return HttpResponse(json.dumps({'status' : 'failed to save model'}), code = 500)
#
#         return HttpResponse(json.dumps({'status' : 'Success'}), code = 200)
