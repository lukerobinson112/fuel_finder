from PyQt4.QtWebKit import QWebView

class Map(QWebView):
    def __init__(self, station1_list, station2_list, station3_list, station4_list, station5_list, station6_list, station7_list, station8_list, station9_list):
        super().__init__()
        self.station1_unleaded = 100
        self.station1_diesel = 200
        self.station1_other = 300
        #this may not be a good idea but I'm gonna do it anyway
        self.page_html = """<!DOCTYPE html>
                            <html>
                              <head>
                                <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
                                <meta charset="utf-8">
                                <title>Custom controls</title>
                                <style>
                                  html, body, #map-canvas {
                                    height: 100%;
                                    margin: 0px;
                                    padding: 0px
                                  }
                                </style>
                                <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
                                <script>
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
                                    var mapDiv = document.getElementById('map-canvas');
                                    var mapOptions = {
                                            zoom: 12,
                                            center: cambridge
                                    };
                              
                              
                                    var map = new google.maps.Map(mapDiv, mapOptions);
                              
                              
                                    var stationLatlng = new google.maps.LatLng(52.21328333333334, 0.13665);
                                    var marker1 = new google.maps.Marker({
                                                    position: stationLatlng,
                                                    map: map,
                                                    animation: google.maps.Animation.DROP,
                                                    title: 'Elizabeth Way BP',
                                            
                                    });
                              
                                    var info1 = new google.maps.InfoWindow({
                                                    content: "<h3>Marker1</h3> <p>Unleaded: """ + str(station1_list[0]) + """ </p> <p>Diesel: """ + str(station1_list[1]) +  """ </p> <p>other: """ + str(station1_list[2]) + """ </p>"
                                    });
                              
                                    var station2Latlng = new google.maps.LatLng(52.21946247877899, 0.11142432689666748);
                                    var marker2 = new google.maps.Marker({
                                            position : station2Latlng,
                                            map: map,
                                            title: 'Histon Rd Esso'
                                    });
                              
                                    var info2 = new google.maps.InfoWindow({
                                            content: "<h3>Marker2</h3> <p>Unleaded: """ + str(station2_list[0]) + """ </p> <p>Diesel: """ + str(station2_list[1]) + """ </p> <p>Other: """ + str(station2_list[2]) + """</p>"
                                    });

                              
                                    var station3Latlng = new google.maps.LatLng(52.198414356177594, 0.11321067810058594);
                                    var marker3 = new google.maps.Marker({
                                            position : station3Latlng,
                                            map : map,
                                            title : 'Newnham Rd Station Shell'
                                    });
                                    
                                    var info3 = new google.maps.InfoWindow({
                                            content: "<h3>Marker3</h3> <p>Unleaded: """ + str(station3_list[0]) + """ </p> <p>Diesel: """ + str(station3_list[1]) + """ </p> <p>Other: """ + str(station3_list[2]) + """ </p>"
                                    });
                              
                                    var station4Latlng = new google.maps.LatLng(52.20019806415637, 0.15837907791137695);
                                    var marker4 = new google.maps.Marker({
                                            position : station4Latlng,
                                            map : map,
                                            title: "Brooks Rd, Sainsbury's"
                                    });
                                    
                                    var info4 = new google.maps.InfoWindow({
                                            content: "<h3>Marker4</h3> <p>Unleaded: """ + str(station4_list[0]) + """ </p> <p>Diesel: """ + str(station4_list[1]) + """ </p> <p>Other: """ + str(station4_list[2]) + """ </p>"
                                    });
                                                                                                       
                                    var station5Latlng = new google.maps.LatLng(52.21112726046464, 0.18126368522644043);
                                    var marker5 = new google.maps.Marker({
                                            position : station5Latlng,
                                            map : map,
                                            title: "Newmarket Rd, Shell"
                                    });
                                    
                                    var info5 = new google.maps.InfoWindow({
                                            content: "<h3>Marker5</h3> <p>Unleaded: """ + str(station5_list[0]) + """ </p> <p>Diesel: """ + str(station5_list[1]) + """ </p> <p>Other: """ + str(station5_list[2]) + """ </p>"
                                    });
                              
                                    var station6Latlng = new google.maps.LatLng(52.17321450649969, 0.11265009641647339);
                                    var marker6 = new google.maps.Marker({
                                            position : station6Latlng,
                                            map : map,
                                            title: "Trumpington, 56 High Street, Shell"
                                    });
                                    
                                    var info6 = new google.maps.InfoWindow({
                                            content: "<h3>Marker6</h3> <p>Unleaded: """ + str(station6_list[0]) + """ </p> <p>Diesel: """ + str(station6_list[1]) + """ </p> <p>Other: """ + str(station6_list[2]) + """ </p>"
                                    });
                              
                                    var station7Latlng = new google.maps.LatLng(52.238283272894094, 0.15647470951080322);
                              
                                    var marker7 = new google.maps.Marker({
                                            position : station7Latlng,
                                            map : map,
                                            title: "Tesco Milton, Tesco"
                                    });
                                    
                                    var info7 = new google.maps.InfoWindow({
                                            content: "<h3>Marker7</h3> <p>Unleaded: """ + str(station7_list[0]) + """ </p> <p>Diesel: """ + str(station7_list[1]) + """ </p> <p>Other: """ + str(station7_list[2]) + """ </p>"
                                    });
                              
                                    var station8Latlng = new google.maps.LatLng(52.25520301641985, 0.019676685333251953);
                              
                                    var marker8 = new google.maps.Marker({
                                            position : station8Latlng,
                                            map : map,
                                            title: "Tesco Bar Hill, Tesco"
                                    });
                                    
                                    var info8 = new google.maps.InfoWindow({
                                            content: "<h3>Marker8</h3> <p>Unleaded: """ + str(station8_list[0]) + """ </p> <p>Diesel: """ + str(station8_list[1]) + """ </p> <p>Other: """ + str(station8_list[2]) + """ </p>"
                                    });
                              
                                    var station9Latlng = new google.maps.LatLng(52.18553665582424, 0.1605302095413208);
                              
                                    var marker9 = new google.maps.Marker({
                                            position : station9Latlng,
                                            map : map,
                                            title: "Cherry Hinton Rd, BP"
                                    });
                                    
                                    var info9 = new google.maps.InfoWindow({
                                            content: "<h3>Marker9</h3> <p>Unleaded: """ + str(station9_list[0]) + """ </p> <p>Diesel: """ + str(station9_list[1]) + """ </p> <p>Other: """ + str(station9_list[2]) + """ </p>"
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



                                </script>
                                    </head>
                                    <body>
                                <div id="map-canvas"></div>
                              </body>
                            </html>"""
                                                               
        #self.page_html.format(str(self.station1_unleaded), str(self.station1_diesel), str(self.station1_other))                                 
        self.setHtml(self.page_html)
