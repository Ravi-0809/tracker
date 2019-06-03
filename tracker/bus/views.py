from django.shortcuts import render
import googlemaps
from django.http import HttpResponse
import json
from bus.models import Bus
from django.views import View
import pytz

def map_bus(request):
    """ Function used to locate a point on the map.

    **TO BE USED ONLY FOR TESTING**

    The function only supports GET method for now. The points to be located are fixed for now.
    The arguments mentioned below are for future use.

    Args:
        latitude (float): Latitude of vehicle to locate.
        longitude (float) : Longitude of vehicle to locate.

    Returns:
        html: renders a html containing the location of the vehicle on a map.

    """

    if(request.method == 'GET'):
        data = {'latitude' : 12.970560, 'longitude' : 77.606750, 'key' : "AIzaSyBEpotTUfU39x1DeZomIQ4tFrRaEXazaaU"}
        return render(request, 'static/map.html', data)
    else:
        return HttpResponse(json.dumps({'status' : 'request method not supported currently'}))

class map_vehicle(View):
    """ Class based view which supports two methods :
            - GET
            - POST
        This class is used by two different clients:
            - **SmartCampus App** uses the *GET* request feature of this view. A get request is made with the
              URL containing the institute ID and the bus number.
            - **Tracker App** updates the location of the bus by sending *POST* requests to the server. This is the
              class that handles those *POST* requests.
    """

    def get(self, **kwargs):
        """The *GET* request requires 2 parameters which are to be proided through the URL. The tracker tab
        in the SmartCampus app is what uses this request.

        Parameters:
            institute_id (int) : Unique identification number of an institute.
            bus_number (int) : The bus number which lets the system know the tracking of which bus needs to be displayed.

        Returns:
            HTML : Renders a HTML page displaying the location of the bus which is uniquely identified by the above two parameters.

        """
        institute_id = self.kwargs['institute_id']
        bus_number = self.kwargs['bus_number']
        qs = Bus.objects.filter(institute__institute_serial_number = institute_id).filter(bus_number = bus_number).latest('timestamp_location')
        latitude = qs.latitude
        longitude = qs.longitude
        location = {'latitude' : latitude, 'longitude' : longitude}

        return render(request, 'static/map.html', location)


    def post(self, request, **kwargs):
        """The *POST* request of this class is used to update the position of a bus. There are two types of arguments
        required for this method:

        - URL parameters
            - institute_id
            - bus_number
        - Request Body Parameters
            - latitude
            - longitude
            - timestamp_location

        Parameters:
            latitude (float) : Latitude of the bus location. Part of the POST request body.
            longitude (float) : Longitude of the bus location. Part of the POST request body.
            timestamp_location (datetime, optional) : In case the location of a bus couldn't be sent due to network issues,
                send the location after receiving network along with the timestamp of when it was recorded. Format - datetime.datetime.now() standard format.

        Returns:
            JSON : The json contains the error or the success message of the procedure. The message can be accessed by accesing the value of the key 'status' in the json.
            The following messages exist:

            - "institute_id does not exist" : incorrect institute_id or institute_id does not exist.
            - "unable to read POST data" : unable to read the data in request body. Send with the exact same parameter names.
            - "error in saving" : unable to save the data.

        """
        institute_id = self.kwargs['institute_id']
        bus_number = self.kwargs['bus_number']
        request_data = json.loads(request.body)

        # -------- Verifying if the institute given exists --------
        try:
            qs = Bus.objects.get(institute__institute_serial_number = institute_id)
            institute_name = qs.institute_name
        except Exception as e:
            return HttpResponse(json.dumps({'status' : 'institute id does not exist'}))

        # ------ Reading the POST data : --------
        try:
            lat = request_data['latitude']
            long = request_data['longitude']
        except Exception as e:
            return HttpResponse(json.dumps({'status' : 'unable to read POST data'}))

        # ------- Save the data to models : ---------
            # ++++ If a certain timestamp is provided for the location +++++++
        if(request_data['timestamp_location']):
            try:
                time_local = request_data['timestamp_location']
                zone = pytz.utc
                time = zone.localize(time_local) # Storing the time as timezone aware time in UTC
                query = Bus(institute__institute_serial_number = institute_id, institute__institute_name = institute_name,
                latitude = lat, longitude = long, timestamp_location = time)
                query.save()
            except Exception as e:
                return HttpResponse(json.dumps({'status' : 'error in saving'}))
            # +++++++ If no timestamp is provided, saves with django.utils.timezone.now() by default +++++++
        else:
            try:
                query = Bus(institute__institute_serial_number = institute_id, institute__institute_name = institute_name,
                latitude = lat, longitude = long)
                query.save()
            except Exception as e:
                return HttpResponse(json.dumps({'status' : 'error in saving'}))
