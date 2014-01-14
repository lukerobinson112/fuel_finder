var map;
var cambridge = new google.maps.LatLng(52.2204385435938, 0.0995635986328125);
var coords = ''

/**
 * The HomeControl adds a control to the map that simply
 * returns the user to Chicago. This constructor takes
 * the control DIV as an argument.
 * @constructor
 */
function HomeControl(controlDiv, map) {

  // Set CSS styles for the DIV containing the control
  // Setting padding to 5 px will offset the control
  // from the edge of the map
  controlDiv.style.padding = '5px';

  // Set CSS for the control border
  var controlUI = document.createElement('div');
  controlUI.style.backgroundColor = 'white';
  controlUI.style.borderStyle = 'solid';
  controlUI.style.borderWidth = '2px';
  controlUI.style.cursor = 'pointer';
  controlUI.style.textAlign = 'center';
  controlUI.title = 'Click to set the map to Home';
  controlDiv.appendChild(controlUI);

  // Set CSS for the control interior
  var controlText = document.createElement('div');
  controlText.style.fontFamily = 'Arial,sans-serif';
  controlText.style.fontSize = '12px';
  controlText.style.paddingLeft = '4px';
  controlText.style.paddingRight = '4px';
  controlText.innerHTML = '<b>Home</b>';
  controlUI.appendChild(controlText);

  // Setup the click event listeners: simply set the map to
  // Chicago
  google.maps.event.addDomListener(controlUI, 'click', function() {
    map.setCenter(cambridge)
  });

}

function initialize() {

	//var price1_u = "1"
	
	var mapDiv = document.getElementById('map-canvas');
	var mapOptions = {
		zoom: 12,
		center: cambridge
	};
	var image = {
        url: 'images/google_blue_small.png',
        //image is 30x51
        size: new google.maps.Size(30, 51),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(0, 51)
    };
	
	var shape = {
      coord: [1, 1, 1, 20, 18, 20, 18 , 1],
      type: 'poly'
    };
  
  
	var map = new google.maps.Map(mapDiv, mapOptions);
  
  
	var stationLatlng = new google.maps.LatLng(52.21328333333334, 0.13665);
	var marker1 = new google.maps.Marker({
			position: stationLatlng,
			map: map,
			animation: google.maps.Animation.DROP,
			title: 'Elizabeth Way BP',
			//icon: image,
			//shape: shape
		
	});
  
	var info1 = new google.maps.InfoWindow({
			content: "<h3>Marker1</h3> <p>Unleaded:" + price1_u + "</p> <p>Diesel: {1}</p> <p>other: {2}</p>"
	});
  
	var station2Latlng = new google.maps.LatLng(52.21946247877899, 0.11142432689666748);
	var marker2 = new google.maps.Marker({
		position : station2Latlng,
		map: map,
		title: 'Histon Rd Esso'
	});
  
	var info2 = new google.maps.InfoWindow({
		content: "<h3>Marker2</h3> <p>Unleaded: {3}</p> <p>Diesel: {4}</p> <p>Other: {5}</p>"
	});

  
	var station3Latlng = new google.maps.LatLng(52.198414356177594, 0.11321067810058594);
	var marker3 = new google.maps.Marker({
		position : station3Latlng,
		map : map,
		title : 'Newnham Rd Station Shell'
	});
	
	var info3 = new google.maps.InfoWindow({
		content: "<h3>Marker3</h3> <p>Unleaded: {6}</p> <p>Diesel: {7}</p> <p>Other: {8}</p>"
	});
  
	var station4Latlng = new google.maps.LatLng(52.20019806415637, 0.15837907791137695);
	var marker4 = new google.maps.Marker({
		position : station4Latlng,
		map : map,
		title: "Brooks Rd, Sainsbury's"
	});
	
	var info4 = new google.maps.InfoWindow({
		content: "<h3>Marker4</h3> <p>Unleaded: {9}</p> <p>Diesel: {10}</p> <p>Other: {11}</p>"
	});
									   
	var station5Latlng = new google.maps.LatLng(52.21112726046464, 0.18126368522644043);
	var marker5 = new google.maps.Marker({
		position : station5Latlng,
		map : map,
		title: "Newmarket Rd, Shell"
	});
	
	var info5 = new google.maps.InfoWindow({
		content: "<h3>Marker5</h3> <p>Unleaded: {12}</p> <p>Diesel: {13}</p> <p>Other: {14}</p>"
	});
  
	var station6Latlng = new google.maps.LatLng(52.17321450649969, 0.11265009641647339);
	var marker6 = new google.maps.Marker({
		position : station6Latlng,
		map : map,
		title: "Trumpington, 56 High Street, Shell"
	});
	
	var info6 = new google.maps.InfoWindow({
		content: "<h3>Marker6</h3> <p>Unleaded: {15}</p> <p>Diesel: {16}</p> <p>Other: {17}</p>"
	});
  
	var station7Latlng = new google.maps.LatLng(52.238283272894094, 0.15647470951080322);
  
	var marker7 = new google.maps.Marker({
		position : station7Latlng,
		map : map,
		title: "Tesco Milton, Tesco"
	});
	
	var info7 = new google.maps.InfoWindow({
		content: "<h3>Marker7</h3> <p>Unleaded: {18}</p> <p>Diesel: {19}</p> <p>Other: {20}</p>"
	});
  
	var station8Latlng = new google.maps.LatLng(52.25520301641985, 0.019676685333251953);
  
	var marker8 = new google.maps.Marker({
		position : station8Latlng,
		map : map,
		title: "Tesco Bar Hill, Tesco"
	});
	
	var info8 = new google.maps.InfoWindow({
		content: "<h3>Marker8</h3> <p>Unleaded: {21}</p> <p>Diesel: {22}</p> <p>Other: {23}</p>"
	});
  
	var station9Latlng = new google.maps.LatLng(52.18553665582424, 0.1605302095413208);
  
	var marker9 = new google.maps.Marker({
		position : station9Latlng,
		map : map,
		title: "Cherry Hinton Rd, BP"
	});
	
	var info9 = new google.maps.InfoWindow({
		content: "<h3>Marker9</h3> <p>Unleaded: {24}</p> <p>Diesel: {25}</p> <p>Other: {26}</p>"
	});


	// Create the DIV to hold the control and
	// call the HomeControl() constructor passing
	// in this DIV.
	var homeControlDiv = document.createElement('div');
	var homeControl = new HomeControl(homeControlDiv, map);
  
	marker1.setAnimation(google.maps.Animation.DROP)
	marker1.setAnimation(google.maps.Animation.BOUNCE)
  
	//javascript:void(prompt('',gApplication.getMap().getCenter()));  USE THIS TO GET CENTRES OF GOOGLE MAPS PAGES
	//http://forums.gpsreview.net/viewtopic.php?t=3632
	
	//MARKER INFOWINDOWS
  
	google.maps.event.addListener(marker1, 'click', function(){
		info1.open(map, marker1);
	});
	
	google.maps.event.addListener(marker2, 'click', function(){
		info2.open(map, marker2)
	});
	
	google.maps.event.addListener(marker3, 'click', function(){
		info3.open(map, marker3)
	});
	
	google.maps.event.addListener(marker4, 'click', function(){
		info4.open(map, marker4)
	});
	
	google.maps.event.addListener(marker5, 'click', function(){
		info5.open(map, marker5)
	});
	
	google.maps.event.addListener(marker6, 'click', function(){
		info6.open(map, marker6)
	});
	
	google.maps.event.addListener(marker7, 'click', function(){
		info7.open(map, marker7)
	});
	
	google.maps.event.addListener(marker8, 'click', function(){
		info8.open(map, marker8)
	});
	
	google.maps.event.addListener(marker9, 'click', function(){
		info9.open(map, marker9)
	});
  
  


	homeControlDiv.index = 1;
	map.controls[google.maps.ControlPosition.TOP_RIGHT].push(homeControlDiv);
}

google.maps.event.addDomListener(window, 'load', initialize);
