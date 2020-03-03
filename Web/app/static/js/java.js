var map = L.map('error').setView([44.5667,6.0833],6);

var tiles = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution:'&copy; <a href="https://ww.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map)

fetch('/static/app1.json')
  .then((response)=>{
    return response.json();
  })
  .then((results)=>{
    var heatMapData = [];
    results.forEach(function(x){
      heatMapData.push(x);
    });
/*    console.log(heatMapData);*/

    var heat = L.heatLayer(heatMapData);
    map.addLayer(heat);
  });
