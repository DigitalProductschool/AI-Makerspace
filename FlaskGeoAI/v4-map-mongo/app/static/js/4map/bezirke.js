/// Bezirke fly to Mapbox


document.getElementById('bezirk').addEventListener('click', function ()
    { 

        var select = document.getElementById('bezirkeham');
        var value = select.options[select.selectedIndex].value;
        if(value == 1){
            locate = [9.934329596, 53.551164462];
        }
        else if(value == 2) {
            locate = [9.994167, 53.550278];
        }
        else if(value == 3) {
            locate = [9.966667, 53.45];
        }
        else if(value == 4) {
            locate = [9.959444, 53.574444];
        }
        else if(value == 5) {
            locate = [9.984, 53.58935];
        }
        else if(value == 6) {
            locate = [10.083333, 53.583333];
        }
        else{
            locate = [10.210278, 53.487222];
        }
        
        
    map.flyTo({zoom: 13,
    center: locate,
    pitch: 40,
    bearing: -180});
});






