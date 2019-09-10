function initMap(linea){
	var map = L.map('map').setView([-53.78903, -67.69588], 14);
	
	L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
      attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
      maxZoom: 17,
      minZoom: 9
	}).addTo(map);

	// load GeoJSON from an external file
	map_file = "";
	if ( linea == "colectivos-rg-all" ) {
		map_file = "/public/colectivos/rio-grande-colectivos-actual-todas-lineas.geojson";
	}
	else {
		map_file = "/public/colectivos/rio-grande-colectivos-actual-" + linea + ".geojson";
	}

/*
	$.getJSON(map_file, function(data){
		// add GeoJSON layer to the map once the file is loaded
		L.geoJson(data, {
			style: function(feature){
				return { color: feature.properties._storage_options.color};
			}
		}).addTo(map);
	});
*/

var jsonMimeType = "application/json;charset=UTF-8";
$.ajax({
 type: "GET",
 url: map_file,
 beforeSend: function(x) {
  if(x && x.overrideMimeType) {
   x.overrideMimeType(jsonMimeType);
  }
 },
 dataType: "json",
 success: function(data){
	L.geoJson(data, {
		style: function(feature){
			return { color: feature.properties._storage_options.color};
		}
	}).addTo(map);
 }
});

	// load GeoJSON from an external file
	//$.getJSON("/public/colectivos/rio-grande-colectivos-paradas.geojson",function(data){
		$.ajax({
			type: "GET",
			url: "/public/colectivos/rio-grande-colectivos-paradas.geojson",
			beforeSend: function(x) {
			 if(x && x.overrideMimeType) {
			  x.overrideMimeType(jsonMimeType);
			 }
			},
			dataType: "json",
			success: function(data){

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
				
				//only show bus stops if they are from this line
				if ( linea != "colectivos-rg-all" && feature.properties.description.indexOf("Línea " + linea.replace("linea-","").toUpperCase()) === -1) {
					return;
				}
				
				var description_linebreaks = feature.properties.description.replace("\nC: ","<br>").split("\n").join("<br>");
				var name = feature.properties.name;
				var marker;
				var has_garita = "";

				if (feature.properties.name.indexOf('Garita') >= 0) {
					marker = L.marker(latlng,{icon: busStopIcon_blue});
					has_garita = "<br>Con garita";
					name = name.replace(" Garita","")
				}
				else{
					marker = L.marker(latlng,{icon: busStopIcon_green});
				}
				
				var must_check = "";
				/*
				if ( !feature.properties.color || feature.properties.color.indexOf("Navy") !== -1 ){
					must_check = "<br> <strong>La parada debe comprobarse</strong>";
				}
				*/
				
				marker.bindPopup(name + has_garita + '<br>' + description_linebreaks + must_check);
				return marker; 
				}
		}).addTo(map);

	}
  });

}