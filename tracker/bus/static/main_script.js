// Header set X-Content-Type-Options "nosniff"
// Initialize and add the map
function initMap()
{
    // The location of the vehicle.
    var loc_of_vehicle = { lat: {{ latitude }}, lng: {{ longitude }} };

    var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 18, center: loc_of_vehicle});
    // The marker, positioned at location of vehicle being tracked
    var marker = new google.maps.Marker({position: loc_of_vehicle,
      map: map,
      label: "Bus"
    });

    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    directionsDisplay.setMap(map);

    // The handler controllling the directions button
    var onClickHandler = function()
    {
      calculateAndDisplayRoute(directionsService, directionsDisplay);
    }
    document.getElementById('dir_button').addEventListener("click", onClickHandler);

    // The handler controllling the marker button
    var onClickHandler_back = function()
    {
          initMap();
    }
    document.getElementById('bus_button').addEventListener("click", onClickHandler_back);

    // The handler controllling the distance matrix button.
    var onClickHandler_distance = function()
    {
          distanceMatrix();
    }
    document.getElementById('dist_button').addEventListener("click", onClickHandler_distance);

}

function distanceMatrix(){
    var origin = { lat : 12.97194, lng : 77.59369};
    var destination = { lat: {{ latitude }}, lng: {{ longitude }} };
    var markersArray = [];
    var service = new google.maps.DistanceMatrixService;
    var destinationIcon = 'https://chart.googleapis.com/chart?' +
            'chst=d_map_pin_letter&chld=D|FF0000|000000';
        var originIcon = 'https://chart.googleapis.com/chart?' +
            'chst=d_map_pin_letter&chld=O|FFFF00|000000';
        var map = new google.maps.Map(document.getElementById('map'), {
          center: destination,
          zoom: 18
        });

    service.getDistanceMatrix({
      origins: [origin],
      destinations: [destination],
      travelMode: 'DRIVING',
      unitSystem: google.maps.UnitSystem.METRIC,
      avoidHighways: false,
      avoidTolls: false
    }, function(response, status) {
      if (status !== 'OK') {
        alert('Error was: ' + status);
      } else {
        var originList = response.originAddresses;
        var destinationList = response.destinationAddresses;
        var startingDiv = document.getElementById('starting');
        var endingDiv = document.getElementById('ending');
        var distanceDiv = document.getElementById('distance');
        var timeDiv = document.getElementById('time');

        startingDiv.innerHTML = "<b>Starting location</b>: My location";
        endingDiv.innerHTML = "<b>Destination</b>: location of vehicle";
        var results = response.rows[0].elements;
        distanceDiv.innerHTML = "<b>Distance</b>: " + results[0].distance.text;
        timeDiv.innerHTML = "<b>ETA</b>: " + results[0].duration.text;


        var showGeocodedAddressOnMap = function(asDestination) {
          var icon = asDestination ? destinationIcon : originIcon;
          return function(results, status) {
            if (status === 'OK') {
              // map.fitBounds(bounds.extend(results[0].geometry.location));
              markersArray.push(new google.maps.Marker({
                map: map,
                position: origin,
                icon: icon
              }));
            } else {
              alert('Geocode was not successful due to: ' + status);
            }
          };
        };
      }
    });
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    var lat_lng_dest = new google.maps.LatLng({ lat: {{ latitude }}, lng: {{ longitude }} });
    var lat_lng_origin = new google.maps.LatLng({ lat : 12.97194, lng : 77.59369});
        directionsService.route({
          // origin: document.getElementById('start').value,
          // destination: document.getElementById('end').value,
          origin: lat_lng_origin,
          destination: lat_lng_dest,
          travelMode: 'DRIVING'
        }, function(response, status) {
          if (status === 'OK') {
            directionsDisplay.setDirections(response);
          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
      }
