function initMap() {
  var map = new google.maps.Map(document.getElementById("map"), {
      zoom: 3,
      center: {
          lat: 40.619261,
          lng: 20.134766
      }
  });

  var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  var locations = [
      { lat: 52.2805888, lng: -9.7024146 },
      { lat: 50.4392466, lng: 30.5076824 },
      { lat: 25.2085411, lng: 55.317125 }
  ];

  var markers = locations.map(function(location, i) {
      return new google.maps.Marker({
          position: location,
          label: labels[i % labels.length]
      });
  });
  var markerCluster = new markerClusterer.MarkerClusterer({ markers, map });
  // var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
}