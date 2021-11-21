// Initialize and add the map
function initMap(latitude=48.85837009999999, longitude=2.2944813) {
    // The location of the eiffel tower
    const tour_eiffel = { lat: latitude, lng: longitude};
    // The map, centered on the eiffel tower
    const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: tour_eiffel,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
    position: tour_eiffel,
    map: map,
    });
}
