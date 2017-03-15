var initMap = function(){
    // grab the map data from it's data attributes
    var data = $('#js-map').data();

    // build some map parameters
    var mapParams = { styles : map_style_dark };
    console.log(data.coords);
    // if coordinates are not in an array, there is only 1 set
    if(! (data.coords instanceof Array)){
        // convert the coordinates to an array with 1 element
        data.coords = [data.coords];
    }

    // set the center of the map if only one set of coords specified
    if(data.coords.length == 1){
        mapParams.center = data.coords[0];
    }

    // add the zoom level to the map params if one was specified
    if(data.zoom){
        mapParams.zoom = data.zoom;
    }

    var map = new google.maps.Map(document.getElementById('js-map'), mapParams);

    // make a new object to keep track of the marker bounds
    var bounds = new google.maps.LatLngBounds();


    data.coords.map((pos, i) => {
        // expand the bounds to include the new marker
        bounds.extend(pos);

        // add a new marker for each item in the list of coordinates
        return new google.maps.Marker({ position: pos, map : map });
    });

    // if there is more than one marker, scale the map to the bounds
    if(data.coords.length > 1){
        map.fitBounds(bounds);
    }
}
