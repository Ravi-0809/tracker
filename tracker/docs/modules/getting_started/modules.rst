Introduction
====================

- This project was developped to track the different vehicles of an institute. This project belongs to SmartCampus of BITS Pilani - Hyderabad Campus.

- The system has the following requirement to function:
    - The backend system built using Django.
    - An app for the users to view the location of the bus and many accompanying features - Integrated into the main **SmartCampus app**.
    - A *Second app* which is installed in a phone that is permanantly fixed in each bus to track. The functions of this app are detailed in the following sections. - **Tracker app**.


Summary of workflow
---------------------

- The workflow of the system is as follows :
    1. The institutes which have agreed to using the system will be registered to the Institute model.
    2. The Tracker app will then be installed in all the vehicles of the institute that are to be tracked. For now, the vehicle numbers will be auto incremented and the same will be used to referrence the vehicle.
    3. The Tracker app will send POST requests to the server transmittting the location of the vehicle at regular intervals of time.
    4. The Backend will process the request and render a HTML page which will have the following information/features:
        - A drop down used to select the vehicle number of the vehicle to appear on the map.
        - Location of the vehicle(whose number is chosen in the drop down) on the map.
        - ETA of bus to users' location.
        - Distance of bus from users' location.
        - Directions of bus from users' location.
