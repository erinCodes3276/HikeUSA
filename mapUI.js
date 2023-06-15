// Initialize and add the map
let map;

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
  map._addListener("click",(mapsMouseEvent) => {
    // Close current info window
    infoWindow.close();
    // Create new
    infoWindow = new google.maps.InfoWindow({
      position: mapsMouseEvent.latLng,
    });
    infoWindow.setContent(
        JSON.stringify(ma)
    )
  })
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "New York",
  });
}

initMap();