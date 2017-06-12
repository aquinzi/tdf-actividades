function initMap(linea){
  var map = L.map('map').setView([-53.78903, -67.69588], 14);
	

  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    {
      attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
      maxZoom: 17,
      minZoom: 9
    }).addTo(map);


  // load GeoJSON from an external file
  $.getJSON("/public/colectivos/rio-grande-colectivos-2016-" + linea + ".geojson", function(data){

    // add GeoJSON layer to the map once the file is loaded
    L.geoJson(data, {
	    style: function(feature){
	       return { color: feature.properties._storage_options.color};
	    }
    }).addTo(map);
  });

  // load GeoJSON from an external file
  $.getJSON("/public/colectivos/rio-grande-colectivos-paradas.geojson",function(data){

	 var busStopIcon_blue = L.icon({
	   iconUrl: '/assets/imgs/bus-stop-blue.png',
	   iconSize: [30,35]
	 }); 

	 var busStopIcon_green = L.icon({
	   iconUrl: '/assets/imgs/bus-stop-green.png',
	   iconSize: [30,35]
	 }); 

    // add GeoJSON layer to the map once the file is loaded
    L.geoJson(data, {
    	
			pointToLayer: function(feature,latlng){
			var marker;

			if (feature.properties.name.indexOf('Garita') >= 0) {
				marker = L.marker(latlng,{icon: busStopIcon_blue});
			}
			else{
				marker = L.marker(latlng,{icon: busStopIcon_green});
			}

			var description_linebreaks = feature.properties.description.replace("\nC: ","<br>").split("\n").join("<br>");
			marker.bindPopup(feature.properties.name + '<br>' + description_linebreaks);
			return marker; 
			}
    }).addTo(map);
  });

}