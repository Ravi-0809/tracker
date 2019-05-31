from django.db import models
import uuid
from authentication.models import Institute

class Bus(models.Model):
    """This model contains the location of a bus.

    The model also contains the intitute to which the bus belongs and also the bus number of a bus in that institute.

    Attributes:
        bus_number (int) : AutoField which stores the bus number of a bus in that institute.
        institute_name (str) : Name of the institute the bus belongs to.
        institute_serial_number (uuid) : unique serial number of the institute the bus belongs to. Stored as a UUID datatype in a postgres database.
        latitude (float) : Stores the latitude of the bus at the given instant.
        longitude (float) : Stores the longitude of the bus at the given instant.

    """
    bus_number = models.AutoField(primary_key = True)
    institute = models.ForeignKey(Institute, on_delete = models.CASCADE)
    latitude = models.DecimalField(max_digits = 9, decimal_places = 6)
    longitude = models.DecimalField(max_digits = 9, decimal_places = 6)

    class Meta():
        app_label = 'bus'
