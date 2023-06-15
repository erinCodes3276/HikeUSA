// Initialize and add the map
let map;
let camps = [];
let trails = [];
async function initMap() {

  // The location of New York
  const position = { lat: 43 , lng: -76 };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map"), {
    zoom: 6.5,
    center: position,
    mapId: "map",
  });


  // Create the initial InfoWindow.
  let infoWindow = new google.maps.InfoWindow({
    content: "Click where you'll be visiting to get recommendations!",
    position: position,
  });

  infoWindow.open(map)
  map.addListener("click",(mapsMouseEvent) => {
    // Close current info window
    infoWindow.close();
    // Create new
    infoWindow = new google.maps.InfoWindow({
      position: mapsMouseEvent.latLng,
    });
    infoWindow.setContent(
        JSON.stringify(mapsMouseEvent.latLng.toJSON(),null, 2)
    );
    infoWindow.open(map);
  });
  //setMarkers(map);
}

initMap();


/*
function setMarkers(map) {

  //import camps from './camps.json' assert {type: 'json'};
  //import trails from './trails.json' assert {type: 'json'};
  //console.log(camps)
  //console.log(trails)
  // Adds markers to the map.
  // Marker sizes are expressed as a Size of X,Y where the origin of the image
  // (0,0) is located in the top left of the image.
  // Origins, anchor positions and coordinates of the marker increase in the X
  // direction to the right and in the Y direction down.
  const image = {
    url: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
    // This marker is 20 pixels wide by 32 pixels high.
    size: new google.maps.Size(20, 32),
    // The origin for this image is (0, 0).
    origin: new google.maps.Point(0, 0),
    // The anchor for this image is the base of the flagpole at (0, 32).
    anchor: new google.maps.Point(0, 32),
  };
  // Shapes define the clickable region of the icon. The type defines an HTML
  // <area> element 'poly' which traces out a polygon as a series of X,Y points.
  // The final coordinate closes the poly by connecting to the first coordinate.
  const shape = {
    coords: [1, 1, 1, 20, 18, 20, 18, 1],
    type: "poly",
  };

  for (let i = 0; i < camps.length; i++) {
    const camps = camps[i];

    new google.maps.Marker({
      position: { lat: camps[1], lng: camps[2] },
      map,
      icon: image,
      shape: shape,
      title: camps[5],
      zIndex: camps[3],
    });
  }
}
*/