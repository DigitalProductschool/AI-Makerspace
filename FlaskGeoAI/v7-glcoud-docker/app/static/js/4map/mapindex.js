mapboxgl.accessToken = '#'; 
/* put your token, looks something like : pk.eyJ1wqf2FsaXwelfnklwfnewbwuuweofheowfhuewgfd024Z3JtIn0.BjfRf3bucp_1yes3_tURwe */

// add the main mapbox map
const map = new mapboxgl.Map({
    container: 'map2', // container ID
    style: 'mapbox://styles/mapbox/light-v10', // style URL
    center: [9.993682, 53.551086], // starting position [lng, lat]
    pitch: 70,
    bearing: -180,
    zoom: 15 // starting zoom
});

//var nav = new mapboxgl.NavigationControl();
//map.addControl(nav, 'bottom-left');

var nav = new mapboxgl.NavigationControl(); // position is optional
map.addControl(nav);

nav._container.parentNode.className="mapboxgl-ctrl-top-center"


// get the menu to change style
const layerList = document.getElementById('menu2');
const inputs = layerList.getElementsByTagName('input');

// change the style of menu onclick()
for (const input of inputs) {
    input.onclick = (layer) => {
        const layerId = layer.target.id;
        map.setStyle('mapbox://styles/mapbox/' + layerId);
    };
}

///////////////////// ADD LAYERS

// add street source for roads, 3dosm onclick
function addSource() {
    map.addSource('mapbox-streets-v8', {
        type: 'vector',
        url: 'mapbox://mapbox.mapbox-streets-v8'});
}

// add the road layer onclick
function addLayer() {
    map.addLayer({
        "id": "road",
        "type": "line",
        "source": "mapbox-streets-v8",
        "layout": {'visibility': 'none'},
        "source-layer": "road",
        "paint": {"line-color": "#CD2956", "line-width": 1}
        });
}

// add the 3D osm building layer
function addLayer2() {
    map.addLayer({
        'id': 'b3D',
        'source': 'composite',
        'source-layer': 'building',
        'filter': ['==', 'extrude', 'true'],
        "layout": {'visibility': 'none'},
        'type': 'fill-extrusion',
        'minzoom': 15,
        'paint': {'fill-extrusion-color': '#555555', 'fill-extrusion-height':
        {'type': 'identity','property': 'height'},
        'fill-extrusion-base': {'type': 'identity','property': 'min_height'},
        'fill-extrusion-opacity': 0.8
        }
    });
}

// add live traffic source
function addSource2(){
    map.addSource('trafficSource', {
        type: 'vector',
        url: 'mapbox://mapbox.mapbox-traffic-v1'
    });
}

// add live traffic data from traffic-layer.js
function addTraffic(){
    var firstPOILabel = map.getStyle().layers.filter(function(obj){ 
        return obj["source-layer"] == "poi_label";
    });
    for(var i = 0; i < trafficLayers.length; i++) {
        
        if (map.getLayer(trafficLayers[i]["id"])) {
            map.removeLayer(trafficLayers[i]["id"]);
        }else{
            map.addLayer(trafficLayers[i], firstPOILabel[0].id);
        }
    }
}

// toggle traffic button to add live traffic data
function addLayer3() {
    var buttonEl = document.getElementById('traffic');
    buttonEl.addEventListener('click', function(e){
        addTraffic();
    });
}

// add atmosphere, 3d terrain source
function addSource3() {
    map.addSource('mapbox-dem', {
        'type': 'raster-dem',
        'url': 'mapbox://mapbox.mapbox-terrain-dem-v1',
        'tileSize': 512,
        'maxzoom': 14
        });
}

// add atmosphere, 3d terrain layer
function addLayer4() {
    map.setTerrain({ 'source': 'mapbox-dem', 'exaggeration': 1.5 });
        
    // add a sky layer that will show when the map is highly pitched
    map.addLayer({
    'id': 'sky',
    'type': 'sky',
    'paint': {
    'sky-type': 'atmosphere',
    'sky-atmosphere-sun': [0.0, 0.0],
    'sky-atmosphere-sun-intensity': 18
    }
    });
}

// add trafic signal lights
function addLayer5() {
    // Add an image to use as a custom marker

   const address = fetch("/data").then((response) => response.json()).then((user) => {
    return user;
  });
  
  const printAddress = async () => {
    const traffic_data = await address;
    map.loadImage(
        'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAXCAYAAAALHW+jAAAACXBIWXMAADByAAAwcgE9juHYAAAGymlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIxLTA5LTI2VDE3OjEyOjAyKzAyOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMS0wOS0yNlQyMToyNTowMiswMjowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMS0wOS0yNlQyMToyNTowMiswMjowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHBob3Rvc2hvcDpJQ0NQcm9maWxlPSJzUkdCIElFQzYxOTY2LTIuMSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo2YmQyMDNmNS0zZDA4LWExNGEtYjJlNi0wZTdlZTQ0NzQ5YmEiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDo1OTdiZjc2Zi0xZTQ3LTczNGQtOThkNy02ODdkNmM1MzY4NTkiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo3ZmVhNTc1MC1lYjY5LWQ1NDEtYTdmMS1mZGViNzQzYTUyN2QiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjdmZWE1NzUwLWViNjktZDU0MS1hN2YxLWZkZWI3NDNhNTI3ZCIgc3RFdnQ6d2hlbj0iMjAyMS0wOS0yNlQxNzoxMjowMiswMjowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo5ZTk5ZDlhNC03MzQyLWM4NDUtOGZjZC1kZjRkZmIxOTdmMTYiIHN0RXZ0OndoZW49IjIwMjEtMDktMjZUMTg6MTg6MDIrMDI6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6NmJkMjAzZjUtM2QwOC1hMTRhLWIyZTYtMGU3ZWU0NDc0OWJhIiBzdEV2dDp3aGVuPSIyMDIxLTA5LTI2VDIxOjI1OjAyKzAyOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+qzWZgQAABgZJREFUOI1dlVtsFNcBhv+ZOXNmds4sa68xa8DrC7FMCbZJ6shuEqkuYJS4LonUFKVEKOUtAZGoiUpAqnigUlFpWrVSkIIqEdQmAilSpFRFiZRaVdOooJISO7ZL4kuL12W9u2QuOzM7szOzc+lD+1I+6X/8nv6Hjzt79iwopRAEAYVCATzP4+TJk9B1Ha1Wa5wQcmbP8PDw5OQkN/3UU18Gvv/Tmzdvfry6uor+/n4wxpAkCQgh/x3ug+M4tFotTlGU73Xk87/xDKNtqVqFf+MGVFkupqL4mGEYL/Ic9879LgAQQsgeQojC83yLUhpSSsM4jn/hN5vT27u6sLJtG+Qowt1SCWcuXEDG99nk5OTbhJDDu4eGfiQIAkmSRCKEiIQQj2ia9idKaV5RFFQqldQwjESSJMGq1/FJvY4jUYTXSyUI+TxOFwp4yzAgcBwIId/Wdf0JjuN4ABwhBKIoGmRpaWleVdVvSZIEwzC4KIoEynFIFQUHAby9sgL09gJvvolL166hdPEiTMbiriDA5/PzgixJIIRAEARwHLdINE07cufOnethGPaIoghVVRFFEcAYxstlpADmHAeb33sPxYUF7E0S/IExDr6PL27fhqIoEEURSZLczefzR0iSJOX19fVHBUG4whibqFsWkiQBBAHXslmcsG08aBhwLl1CCuDPmQw6CEEUx9jY2ABjDKIo/iWKoudUVS3zIyMjGBwc3LBt+weVSuVetVJBK03RFUX4NJfDd/r6MZuRYEoinuvuxkx7O3qTBGGa8s1mE5qmfVWpVI6Ojo6WDx06BMIYw/j4OGRZLjHGdvu+nywsLPyuxQvT/YGHWVHAo3IPAB5EjtFW19BwXR7AB/v27Xu+vb0dQRDoU1NT6OjoAGk2m08TQjqmpqaaAwMDuiiK+rFjx5llG+jp60VlleKhwQBprGP5topNXR1oeA7iOGanTp3q27JlS75UKm0ul8sZy7J0omnabymluXq9jrW1NeRyOUiShCiM8eU/Uxw/quPc0Sr4XD9+/BbBz8+ZeGSUT1RV/ebMzB//niQpeJ4HpRSiKFqCoigjrusOu66LZrMJx3FQqZRgO8D3n5Zw8cwqTLMf6tBlHJhsYPb6DDTn62lWDbC2dpezbRu2bcMwDGia9ntiGMbxOI57KaWPybIMUaRI0xRABn35GhADG9UNWH89hweGlvHwDuCjLxhSeFheXgJjDDzPg+f5G52dnccESZL8ZrN5OQiCQd/3hxsNB1EUIYx5VPUcDj7uYGefj2y0hFag4bVfqdjW81CSxjZu3ZrjwzBAGIZXoyialmW5yY+NjUFV1VTX9VdqtdpcrVYz4hhhR1uMf1VkPPlSL97/mOFvJQVPvlDE7D8YtnclQhQhbrVC3TTNz6vV6quMsXT//v0gAwMDKBaLmJ+fry0uLj6sKAo8z7uSJOLhXTuB9Q0Jh0/sgAAgzcfo7tFh1RuQZfn9gYGBZzVNw969ezExMYHOzk4Qy7JezGQyubGxMe/AgQOmoij++fPnd+mWge1tWzEIDuZEAiO0sWVJgO/JsJsORE7cefr06UMAaBzH7WmaMtM0LVKr1X5GKc2Joghd15HL5aAoGWiahvheiPILCSrPJ3igew9w2Yb1yhxILCREJiOLi4vv/u8QCIIASqklyLLc12g0HnFdF57nwbEdrFf/Dd6OITybx/rLFgpfFfDazldhfgOYu/UJxszdqbcpwtrqHc6smzBNE4ZhoFarvUNc131Z07RuSZKmM5kMqEiRJilkUOi8BiALXXPwxswbuLerDnRFkB0FdmpjZWUFClNACAHP8x8WCoUTwtatW2PXda80Gg3F87zHHcdBHMfgiYjNd1V4/THC0RSaVIK/5qLt1yKGHxxKrMDG7GezfBiG8DzvdUmSjhaLxViglML3fQRBcMv3/VHf9zOSSFkqg+tAHm3XOSAGWC2L7l9K4Jdb2DHxNd7RLSwtL1eCIPg0TdMfEkKaURSBuz9QHMehPZ8/w4F7iWSIzbtcJBkcB6QIs2l6L9HJMwe/uymbzV64evXqTxqNxv9F6j9WTuhF3YOOXwAAAABJRU5ErkJggg==',
        (error, image) => {
        if (error) throw error;
        map.addImage('custom-marker', image);


        // Add a GeoJSON source with 2 points
        map.addSource('points', {
            'type': 'geojson',
            'data': {
            'type': 'FeatureCollection',
            'features': traffic_data
            }
            });
            
        // Add a symbol layer
        map.addLayer({
            'id': 'signal',
            'type': 'symbol',
            'source': 'points',
            'layout': {
            'icon-image': 'custom-marker',
            'visibility': 'none',
            // get the title name from the source's "title" property
            'text-field': ['get', 'title'],
            'text-font': [
            'Open Sans Semibold',
            'Arial Unicode MS Bold'
            ],
            'text-offset': [0, 1.25],
            'text-size': 8,
            'text-anchor': 'top'
            }
        });
        
    }); 

  };
  printAddress();
    
}

function WeatherSource() {
    fetch("https://api.openweathermap.org/data/2.5/weather?q=Hamburg&units=metric&appid=yourappidhere").then((response) => response.json()).then((user) => {
        let temp = user.main.temp;
        let feels_like = user.main.feels_like;
        let wind = user.wind.speed;
        let desc = user.weather[0]["description"];
        document.getElementById("temp2").innerHTML = "Temp: "+ temp +' °C';
        document.getElementById("feels").innerHTML = "Feeling Like: "+feels_like +' °C';
        document.getElementById("wind").innerHTML = "Wind Speed: "+wind +' m/s';
        document.getElementById("desc2").innerHTML = "Description: "+desc;
      });
}

function BezirkeSource() {
    // Add a data source containing GeoJSON data.
    map.addSource('maine', {
    'type': 'geojson',
    'data': {
        'type': 'FeatureCollection',
        'features': hamburg
        }
    });
}

function BezirkeLayer(){
    map.addLayer({
        'id': 'maine',
        'type': 'fill',
        'source': 'maine', // reference the data source
        "layout": {'visibility': 'none'},
        'paint': {
        'fill-color': '#6bbac9', // blue color fill
        'fill-opacity': 0.1
        }
        });
        // Add a black outline around the polygon.
    map.addLayer({
        'id': 'outline',
        'type': 'line',
        'source': 'maine',
        "layout": {'visibility': 'none'},
        'paint': {
        'line-color': '#000',
        'line-width': 0.5
        }
    });
}

const targetDiv = document.getElementById("weather");
const btn = document.getElementById("temptemp");
btn.onclick = function () {
  
  if (targetDiv.style.display !== "none") {
    targetDiv.style.display = "none";
  } else {
    targetDiv.style.display = "block";
  }
};



map.on('style.load', () => {
    const styleJson = map.getStyle();
    if(styleJson["name"] === 'Mapbox Satellite'){
        addSource(); // street-v8 for road-3D OSM
        addSource2(); // live traffic source
        addSource3(); // 3D terrain, atmosphere
        addLayer(); // road layer
        addLayer3(); // traffic layers
        addLayer4(); // 3D terrain, atmosphere
        addLayer5(); // traffic signal lights
        WeatherSource();
        BezirkeSource();
        BezirkeLayer();
    }
    else{
        addSource(); // street-v8 for road-3D OSM
        addSource2(); // live traffic source
        addSource3(); // 3D terrain, atmosphere
        addLayer(); // road layer
        addLayer2(); // 3D OSM
        addLayer3(); // traffic layers
        addLayer4(); // 3D terrain, atmosphere
        addLayer5(); // traffic signal lights
        WeatherSource();
        BezirkeSource();
        BezirkeLayer();
    }

});


map.on('click', 'maine', (e) => {
    new mapboxgl.Popup({closeButton: false, closeOnClick: true, closeOnMove: true})
    .setLngLat(e.lngLat)
    .setHTML(e.features[0].properties.Stadtteil)
    .addTo(map);
});


var buttonE5 = document.getElementById('bezirke22');
buttonE5.addEventListener('click', function(e){
var layerid3 = ['maine', 'outline']
for(let u=0; u< layerid3.length; u++)
    if (map.getLayer(layerid3[u])["visibility"]=="none") {
        map.setLayoutProperty(layerid3[u], 'visibility', 'visible');
    }else{
        map.setLayoutProperty(layerid3[u], 'visibility', 'none');
    }
});


// add toggle button for the layers road, 3D and signal
map.on('idle', () => {
    if (!map.getLayer('road')) {
        return;
        }
    const toggleableLayerIds = ['road', 'b3D', 'signal'];
    let count = 0;
    // Set up the corresponding toggle button for each layer.
    for (const id of toggleableLayerIds) {
        
        // Skip layers that already have a button set up.
        if (document.getElementById(id)) {
        continue;
        }
        
        // Create a link.
        //const roaddiv = document.getElementById('roads2').childNodes[0];
        const link = document.createElement('a');
        link.id = id;
        link.href = '#';
        link.textContent = id;
        link.className = 'active';
        link.style = 'color: red';
        
        // Show or hide layer when the toggle is clicked.
        link.onclick = function (e) {
        const clickedLayer = this.textContent;
        e.preventDefault();
        e.stopPropagation();
        
        const visibility = map.getLayoutProperty(
        clickedLayer,
        'visibility'
        );
        
            // Toggle layer visibility by changing the layout object's visibility property.
            if (visibility === 'visible') {
                map.setLayoutProperty(clickedLayer, 'visibility', 'none');
                this.className = '';
            } else {
                this.className = 'active';
                map.setLayoutProperty(
                clickedLayer,
                'visibility',
                'visible'
                );
            }
        };

        if(count == 0){ var idht = 'roads2';}
        else if(count == 1) { var idht = 'osm3d';}
        else {
            var idht = 'points_signal';
        }
        const layers = document.getElementById(idht);
        layers.appendChild(link);
        count++;
        }
});
            



