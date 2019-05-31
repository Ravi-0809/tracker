from django.db import models
import uuid

class Institute(models.Model):
    """Contains the information of Institutes registered for the tracker.

    Attributes:
        institute_name (str) : Name of the institute the bus belongs to.
        institute_serial_number (uuid) : unique serial number of the institute the bus belongs to. Stored as a UUID datatype in a postgres database.

    """
    institute_name = models.CharField(max_length = 100)
    institute_serial_number = models.UUIDField(default = uuid.uuid4, editable = False)

    class Meta():
        app_label = 'authentication'

class User(models.Model):
    """Contains the information of the users using the tracking feature.

    Attributes:
        user_name (str) : Name of the user. Max length = 100.
        institute (ForeignKey) : Foreign key to the *Institute* model. Therefore, one user can only be a part of one institute.
        latitude (float) : Stores the latitude of the bus at the given instant. Defaulted to null as we're not sure if we want to save the location of a user.
        longitude (float) : Stores the longitude of the bus at the given instant. Defaulted to null as we're not sure if we want to save the location of a user.

    """
    user_name = models.CharField(max_length = 100)
    institute = models.ForeignKey(Institute, on_delete = models.CASCADE)
    latitude = models.DecimalField(max_digits = 9, decimal_places = 6, default = None)
    longitude = models.DecimalField(max_digits = 9, decimal_places = 6, default = None)

    class Meta():
        app_label = 'authentication'
