let container = {};
const searchInput = document.getElementById('search');
let textBar = document.getElementById('text-bar');

function fetchData() {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', '/cities');
  xhr.onload = function() {
    if (xhr.status === 200) {
      const data = JSON.parse(xhr.responseText);
      console.log(data);
      container.data = data;
      // get keys from data, data is just a map
      const categories = Object.keys(data);
      
      const datalist = document.createElement('datalist');
      datalist.id = 'categories';

      categories.forEach((category) => {
        const option = document.createElement('option');
        option.value = category;
        datalist.appendChild(option);
      });

      document.body.appendChild(datalist);
      document.getElementById('search').setAttribute('list', 'categories');
    } else {
      console.error('Request failed. Returned status of ' + xhr.status);
    }
  };
  xhr.send();
}

window.addEventListener('load', function() {
  fetchData();
})

var map = L.map("map").setView([37.9715, 23.7251], 3);
L.tileLayer('https://{s}.tile.thunderforest.com/transport/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: 'Map data &copy; <a href="https://www.opencyclemap.org/">OpenCycleMap</a>',
}).addTo(map);

// function that takes data as an input (map)
// loop through the data and takes latitude and longitude
// then add marker with those coordinates to the map
function addMarkers() {
  // remove all markers
  map.eachLayer((layer) => {
    if (layer instanceof L.Marker) {
      map.removeLayer(layer);
    }
  });
  // add markers
  const searchTerm = searchInput.value;
  const cities = Object.keys(container.data);
    const categoryData = container.data[searchTerm];
    categoryData.forEach((item) => {
        const marker = L.marker([item.latitude, item.longitude]).bindPopup(item.place_name).addTo(map);
        container.coordinates = [item.latitude, item.longitude];
        marker.on('click', function(e) {
          textBar.textContent = item.description;
        });
    });
    map.setView([container.coordinates[0], container.coordinates[1]], 10);
}

document.getElementById('search-btn').addEventListener('click', function() {;
  addMarkers();
  document.getElementById('search').disabled = false;
})